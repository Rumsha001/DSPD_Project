# DSPD_Project

Colab Link: https://colab.research.google.com/drive/15v4FWvvAofVX_T-TupY1vBlHKKe5-5Q6?usp=sharing 

## Weather Forecasting Application
Weather forecasting is the application of scientific techniques and technology to predict the conditions of the atmosphere at a certain location and time. Weather Forecasting in old time is carried out by hand, using changes in barometric pressure, current weather conditions, and sky condition or cloud cover, weather forecasting now relies on computer-based models that take many atmospheric factors into accounting now relies on computer-based models that take many atmospheric factors into account. 
Our main goal is to analyze how the different machine learning techniques will perform in the forecasting of weather combining time series with the neural network.

## DATA SET
The dataset that has been picked from World Weather Online website. 
It provides us historical data as well as gives us information with respect to location that we choose. Here, “Karachi, Pakistan” data has been collected.  
The source data contain various features that can help to find optimum prediction for the data. 
Moreover, time-series data is used to obtain accuracy and apply some advance Machine Learning and Deep Learning algorithms.
Through their API, last 11 years historical data has been fetched.
After which we have converted the JSON response into .csv format, segregating it into each year’s file.
All of these files have been stored in Amazon S3 Bucket. By using boto3, the csv data was called from S3 and converted it into our dataset. 
Dataset consists of following files:
  Elements: date, time, temperature, feels like, humidity, dew point, wind speed, wind direction etc.
  Format: .csv format.
  Date Range: 2010-2020

## Models

### 1)	Random Forest:
A random forest is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.
Analysis: The difference between the actual and predicted values is the very minor, so this model could be used for the out of sample predictions.

###  2)	Decision Tree:
Decision tree builds regression or classification models in the form of a tree structure. It breaks down a dataset into smaller and smaller subsets while at the same time an associated decision tree is incrementally developed.
Analysis: This model mapped the predicted values accurately and hence the difference between actual and predicted values was almost equal to zero. The model seems to be prefect to predict the out of sample values, but this may have an overtraining issue as this is perfectly mapping the training data.

### Time-Series Models
### 3)	Prophet: Automatic Forecasting Procedure
Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well.


### 4)	Long Short-Term Memory
Long short-term memory (LSTM) is an artificial recurrent neural network (RNN) architecture used in the field of deep learning. An LSTM is generally used favorably for time-series data (such as our precipitation datasets) as it is able to ‘remember’ long-term dependencies/information from a feature called cell state. This cell state runs across the networks and passes down (or up) information such that earlier information from a sequence, for instance, could influence prediction of later input. This passing of information is crucial for time-series weather data where each input is dependent on other input from varying time points. The information that is stored, removed, modified, and passed around is controlled by gates. 

To perform weather forecasting in a timely and efficient manner, it is critical to understand the model and examine it in different ways to achieve highest accuracy without overfitting the model. Hence, in order to improve the predicted outcome, further analysis will be done.

## API Setup
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python.
It is used in this project as the model is exported and wrapped around Fast API.
Through which, using Fast API’s endpoint will be able to receive date for which prediction is required and will return output to the user.


## Dockerization
Docker is an open platform for developing, shipping, and running applications. Dockerization enables you to separate your applications from your infrastructure so you can deliver software quickly.
As per the requirement, a docker image has been created in which all the necessary libraries are mentioned to be installed under the dockerfile.
Currently, forecast analysis that is done using Prophet is only dockerized.
