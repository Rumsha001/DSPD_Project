from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pickle
import numpy as np
import pandas as pd
import fbprophet
import os
import io
import re

APP_ROOT = os.path.dirname(os.path.realpath(__file__))
MODEL_PATH = '/'.join([APP_ROOT, 'model.pkl'])
templates = Jinja2Templates(directory=f'{APP_ROOT}/templates')

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return "Use /prophet/{date} for prediction"


@app.get("/prophet/{date}", response_class=HTMLResponse)
def predict_prophet(request: Request, date: str):
    prediction = get_prediction(date)
    context = {'request': request, 'table': prediction}
    return templates.TemplateResponse('prediction.html', context)


def get_prediction(date):
    loaded_model = pickle.load(open(MODEL_PATH, 'rb'))
    future = list()
    future.append(date)
    # for i in range(1, 13):
    #     date = '2021-%02d' % i
    #     future.append([date])
    future = pd.DataFrame(future)
    future.columns = ['ds']
    future['ds'] = pd.to_datetime(future['ds'])
    print(future)
    res = loaded_model.predict(future)
    print(res)
    html_updated = res.to_html(classes=["table", "table-hover", "table-responsive"])
    print(html_updated)
    return html_updated
