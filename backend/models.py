# models.py
# Interacts with Database, uses Flask and SQLAlchemy within a Python Class
# -------------------------------------------------------------------------------------------------------------------------------
# Relative import - Instance access to SQLAlchemy
from config import db

# Inherit Database Model as a Python Class
class Contact(db.Model):
    # Always need an "id" for ALL Database Instances (Auto Generated)
    # primary_key (True): Must be unique in every entry of Database
    id = db.Column(db.Integer, primary_key = True)

    # db.String(80): Specifiy String length of Column
    # nullable (False): Cannot pass a NULL value
    first_name = db.Column(db.String(80), unique = False, nullable = False)
    last_name = db.Column(db.String(80), unique = False, nullable = False)
    
    # unique (True): No two Contacts can have the same email
    email = db.Column(db.String(120), unique = True, nullable = False)

    # Define a function:
    # Convert all field data into a Python Dictionary then convert into JSON which can be passed into the API
    def to_json(self):
        # When using JSON, use Camel Case fields:
        # Lower: The first letter of the first word is lowercase (Ex: myVariableName).
        # Upper: The first letter of every word is uppercase (Ex: MyVariableName).
        
        # When using Python, use Snake Case fields:
        # Words in a variable or field name are separated by underscores and written in lowercase.
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }