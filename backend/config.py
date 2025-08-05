# config.py (Built First)
# Main configuration of our application
# -------------------------------------------------------------------------------------------------------------------------------
# Building the API:
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Flask Application
app = Flask(__name__)

# Wrap App under CORS
CORS(app)

# Initialize Database
# Creates a Database File at location = "Name"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

# Track Modifications (Disabled for now)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create Instance of Database - Allows us to use CRUD Method (Create, Read, Update, Delete)
db = SQLAlchemy(app)