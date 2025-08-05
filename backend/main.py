# main.py
# Main routes and Endpoints (Multiple files if big project)

# To Test your API, use "POSTMAN":
# http://127.0.0.1:5000
# http://127.0.0.1:5000/contacts
# http://127.0.0.1:5000/create_contact
# http://127.0.0.1:5000/update_contact/<int:user_id>
# http://127.0.0.1:5000/delete_contact/<int:user_id>

# Server Address:
# Local Machine: localhost:5000
# Endpoint: /home
# Domain or URL: google.com

# CRUD Operations - Create, Read, Update and Delete:
# REQUEST ->
# type: GET - Access, POST - Create, PUT/PATCH - Update, DELETE
# json: {Data}
# Ex: Create
#       - first_name
#       - last_name
#       - email

# Response ->
# Status: 404 (Not Found), 400 (Bad), 403 (Forbidden/Unauthorized)
# json: {Data}
# ----------------------------------------------------------------------------------------------------------------------------

# jsonify: Return json Data
from flask import request, jsonify
from config import app, db
from models import Contact
# ---------------------------------------------------------------------------------------------------------------------------
# GET Method:
# Decorator
@app.route("/contacts", methods = ["GET"])
def get_contacts():
    contacts = Contact.query.all()
    
    # Convert the Map of all contacts into a List
    json_contacts = list(map(lambda x: x.to_json(), contacts))

    # Dictionary list of contacts converted to JSON by jsonify
    return jsonify({"contacts": json_contacts})                     # Status Code: "200" by default
# ---------------------------------------------------------------------------------------------------------------------------
# POST Method:
@app.route("/create_contact", methods = ["POST"])
def create_contacts():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    
    # 400 Error Status when Contacts don't include all variables
    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a first name, last name, and email"}),
            400,
        )
    
    # Create a new contact with different fields
    new_contact = Contact(first_name = first_name, last_name = last_name, email = email)

    try:
        # Add to the Database Session (Staging Area)
        db.session.add(new_contact)
        # Actually writes everything from the Staging Area into the Database permanently
        db.session.commit()
    except Exception as e:
        # 400 Bad Request Error
        return jsonify({"message": str(e)}), 400
    
    # 200 (OK) Status Code | 201 (Created) Status Code
    return jsonify({"message": "User created!"}), 201
# ---------------------------------------------------------------------------------------------------------------------------
# Update Method:
@app.route("/update_contact/<int:user_id>", methods = ["PATCH"])        # Could be either: POST/PATCH
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    
    # 404 Status Code: "Not Found" (No Contact Found)
    if not contact:
        return jsonify({"message": "User not found"}), 404
    
    # Parse thru JSON Data
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    # Modify the Contacts:
    # Since contact already existed & added into Session, changes can be made permanently
    db.session.commit()

    return jsonify({"message": "User Updated"}), 200
# ---------------------------------------------------------------------------------------------------------------------------
# DELETE Method:
@app.route("/delete_contact/<int:user_id>", methods = ["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)
    
    # 400 Not Found Error: Contact Not Found, therefore cannot DELETE
    if not contact:
        return jsonify({"message": "User Not Found"}), 400
    
    # Delete the contact
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User Deleted"}), 200
# ---------------------------------------------------------------------------------------------------------------------------
# If we input the files don't do this, otherwise run file directly
# Do we have the Database already? if not, create it then we run the app
if __name__ == "__main__":
    # Instantiate Database:
    # Get context of app
    with app.app_context():
        # Create all different models we have defined in Database
        db.create_all()
    app.run(debug = True)
# ----------------------------------------------------------------------------------------------------------------------------