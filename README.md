Sample project for data engineer (A), data analyst (B), analytics engineer (C), data scientist (D) or similar.

1. Write Python code to fetch the data for the latest month and store it on your local disk and uncompress it. (A, C, D)
0. Data cleansing: identify data quality issues in the data and make a plan (or code) to delete the incomplete/inconsistent data (see task 3/4) (A, B, C, D)
0. Design 1 or more database tables to store the data downloaded in Task 1. Show the DDL, including indexes. (A, B, C, D)
0. Load the data that has been cleaned into a local Postgres database (preferably containerized) for later querying. Show the code / method used to do this. (A, B, C, D)
0. Design and implement an ETL process that watches the source website for new data and automatically downloads, cleans and loads the new data into the Postgres database. Show how you handle errors (e.g., connection drops while downloading the data, download is corrupted) and any re-try logic. (A, C)
0. Assume that the ETL process crashes midway. Show how you will resume the ETL correctly when the process is restarted. (A, C)
0. Containerize your ETL code (write the Dockerfile, push to Dockerhub) (A)
0. Explain (do not implement) the tools/services you would use in production version of this ETL task. How do you monitor the ETL for failures? For data quality issues? (A)
0. Make sure your database has at least a few (ideally 12 or more) months of data. Examine/Play around with the data. Write some SQL queries that will show some interesting stats (average ride duration, peak duration, most popular borrowing station, most popular returning station, etc..). The more interesting, the better. (A, B, C, D)
0. Write queries for the following and show the tabular output (B, C, D)
    1. Find the station id with the most ride minutes by month
    0. Find the origin station with the most originations (count).
    0. For each week of the year, derive the total and average ride durations for casual and members each.
    0. What are some of the most popular trips (start station/end station pairs) that most members took?
0. Using a BI tool such as Tableau Public, visualize the following: (B, C, python notebook for D ok)
    1. On the San Francisco Bay Area map, show the intensity of rides (borrows) at every station. A drop down should enable selection of the month.
    0. On the SF Bay Area map, show the top 5 stations by rides initiated. Allow selection by month, subscription status
    0. Visualize week over week/month over month change in rides. Allow selection by station, member status.
0. For Task 10 or 11, design some derived tables that can simplify the creation / development of dashboards. How would you maintain the derived tables (e.g., DBT). Explain clearly (schedule, clean vs incremental, data freshness concerns) the choices and tools (DBT, Glue, ETL, etc) that you will use. (A, C)
0. Perform some cohort analysis (B, D)
    1. By first seen month: how many rides, ride minutes in subsequent months
    0. By bike type, member status
0. Exploratory data analysis (D)
    1. Perform some statistical tests for the categories (member status, bike type)
    0. What is the distribution of categorical and discrete variables like user type, bike type
    0. What is the optimal number of bikes in the system?
    0. Any obvious patterns and correlations ? (time of ride, casual vs member	)
    0. Histogram of time (hour) of ride start and station
    0. Distribution of minutes per ride
    0. Should there be more bikes at certain stations at certain times of the day? (assume that the number of bike slots at a station is the peak number of rides that day)
0. Machine Learning (D)
    1. Predict the duration of a ride given member status, type of bike, time of day, starting station. Use at least 2 ML methods for prediction and compare the accuracy. 
    0. Given a ride (duration, start station, miles, start time), predict the type of bike, and member status
    0. Are there any lost bikes? (bikes that are never returned). Predict the probability of a lost bike for a given ride start. 
    0. Any other interesting anomalies/classification/
 