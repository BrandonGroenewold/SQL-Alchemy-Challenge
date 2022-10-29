# Climate and Station Analysis

## Skills used: SQL Alchemy, Python 

## (If you want to recreate) Before You Begin

1. Create a new repository for this project and name it what you like.

2. Clone the new repository to your computer.

3. Add your Jupyter notebook and `app.py` to this folder. These will be the main scripts to run for analysis.

4. Push the changes to GitHub.

![surfs-up.png](Images/surfs-up.png)

## Overview

I will look at the climate around Hawaii to see if when a good time to take a vacation is.

### Part 1: Climate Analysis and Exploration

In this section, I used Python and SQLAlchemy to perform basic climate analysis and data exploration of my climate database. I completed the following tasks by using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* First I used SQLAlchemy’s `create_engine` to connect to my SQLite database.

* Then I used SQLAlchemy’s `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

* After that Python was used to link the database by creating a SQLAlchemy session.

* At the end of the notebook I closed my session. This is important to do!

#### Precipitation Analysis

To perform an analysis of precipitation in the area, I did the following:

* I found the most recent date in the dataset.

* Using this date, I retrieved the previous 12 months of precipitation data by querying the 12 previous months of data. **Note:** If you do this, do not pass in the date as a variable to your query.

* Then I performed these steps

* selected only the `date` and `prcp` values.

* Loaded the query results into a Pandas DataFrame, and set the index to the date column.

* Sorted the DataFrame values by `date`.

* Plotted the results by using the DataFrame `plot` method, as shown in the following image:

  ![precipitation](Images/precipitation.png)

* At the end used Pandas to print the summary statistics for the precipitation data.

#### Station Analysis

In order to perform an analysis of stations in the area, I did the following:

* Designed a query to calculate the total number of stations in the dataset.

* Designed a query to find the most active stations (the stations with the most rows).

    * Listed the stations and observation counts in descending order.

* Finally I designed a query to retrieve the previous 12 months of temperature observation data (TOBS).

    * Filtered by the station with the highest number of observations.

    * Queried the previous 12 months of temperature observation data for this station.

    * Plotted the results as a histogram with `bins=12`, as shown in the following image:

    ![station-histogram](Images/station-histogram.png)

* Close out your session.

- - -

### Part 2: Design Your Climate App

Now that I have completed your initial analysis, I’ll design a Flask API based on the queries that you have just developed.

Use Flask to create routes, as follows:

* `/`

    * Homepage.

    * List all available routes.

* `/api/v1.0/precipitation`

    * Converted the query results to a dictionary using `date` as the key and `prcp` as the value.

    * Returned the JSON representation of your dictionary.

* `/api/v1.0/stations`

    * Returned a JSON list of stations from the dataset.

* `/api/v1.0/tobs`

    * Queried the dates and temperature observations of the most active station for the previous year of data.

    * Returned a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

    * Returned a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.
