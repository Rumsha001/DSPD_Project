# DSPD_Project

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
ѻ	Elements: date, time, temperature, feels like, humidity, dew point, wind speed, wind direction etc.
ѻ	Format: .csv format.
ѻ	Date Range: 2010-2020

## Models

## API Setup

## Dockerization
