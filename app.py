#Import dependencies
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
import numpy as np
import pandas as pd
from time import strptime

#------------ #Database setup -------------------------
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


#---------------Flask setup ------------------------------
#Create Flask
app = Flask(__name__)

#Flask routes 
@app.route("/")
def home():
   
    return(
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/temp/start/end<br/>'
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year from the last date in data set.
    previous_date= dt.date(2017,8,23)

    one_year = dt.timedelta(days=365)
    prior_year = previous_date - one_year

    # Perform a query to retrieve the data and precipitation scores
    precipitation_scores = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>= prior_year).all()
    session.close()
    #Dictionary with date as a key and precipitation as a value
    precip_results= {date:prcp for date, prcp in precipitation_scores}

    return jsonify(precip_results)
    

@app.route("/api/v1.0/stations")
def stations():
    #Query
    total_stations = session.query((Station.station)).all()

    session.close()
    #Return results
    stations = list(np.ravel(total_stations))
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def tobs():
   #Query
    previous_date = dt.date(2017,8,23)

    one_year = dt.timedelta(days=365)
    prior_year = previous_date - one_year

    active_stations = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= prior_year).all()
    session.close()
    temps = list(np.ravel(active_stations))
    return jsonify(temps = temps)

@app.route("/api/v1.0/temp/<start>/<end>")
def tempstartend(start, end):
    format_date = "%Y,%m,%d"
    results_start_end = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),\
        func.avg(Measurement.tobs)).filter(Measurement.date >= dt.datetime.strptime(start,format_date)).filter(Measurement.date <= dt.datetime.strptime(end, format_date)).all()
    session.close()
    results = list(np.ravel(results_start_end))
    print(results)
    return jsonify(results = results)

#Run Flask
if __name__ == "__main__":
    app.run(debug=True)

