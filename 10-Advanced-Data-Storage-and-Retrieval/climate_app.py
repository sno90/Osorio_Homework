# import dependencies
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import sqlalchemy
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Python SQL toolkit and Object Relational Mapper

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
#session = Session(engine)

#################################################
# Flask Routes
#################################################
app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/start_date</br>"
        f"/api/v1.0/end_date"
    )


@app.route("/api/v1.0/precipitation")
def prcp():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    end_date = '2017-08-23'
    start_date = '2016-08-23'

    results = session.query(Measurement.date, Measurement.prcp).filter(
        Measurement.date <= end_date, Measurement.date >= start_date).all()

    session.close()

    # Convert list of tuples into normal list
    prcp_year = list(np.ravel(results))

    return jsonify(prcp_year)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()

    # Convert list of tuples into normal list
    stations = list(np.ravel(results))
    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def temperatures():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    end_date = '2017-08-23'
    start_date = '2016-08-23'
    results = session.query(Measurement.date, Measurement.tobs).filter(
        Measurement.date <= end_date, Measurement.date >= start_date).all()

    # close session
    session.close()

    # Convert list of tuples into normal list
    temp = list(np.ravel(results))
    return jsonify(temp)


# @app.route("/api/v1.0/start_date")

if __name__ == '__main__':
    app.run(debug=True)
