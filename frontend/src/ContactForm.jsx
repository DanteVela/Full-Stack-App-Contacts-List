// Create a Form
import { useState } from "react"

const ContactForm = ( existingContact = {}, updateCallback) => {
    // Store the contents of a Contact
    const [firstName, setFirstName] = useState(existingContact.firstName || "")
    const [lastName, setLastName] = useState(existingContact.lastName || "")
    const [email, setEmail] = useState(existingContact.email || "")

    // At least one contact exists: Update | Otherwise: Create a new contact
    const updating = Object.entries(existingContact).length !== 0

    // onSubmit Function for Create Button
    const onSubmit = async (e) => {
        // Do not refresh the page automatically
        e.preventDefault()

        // Setup POST Request:
        // "data" is a JavaScript Object
        const data = {
            firstName,
            lastName,
            email
        }
        const url = "http://127.0.0.1:5000/" + (updating ? `update_contact/${existingContact.id}`: "create_contact")
        const options = {
            // Specify the method options unless its a GET Request (Automatically)
            method: "POST",

            // So the API knows we have JSON data to submit
            headers: {
                "Content-Type": "application/json"
            },

            // Convert "data" into JSON
            body: JSON.stringify(data)
        }

        // Send the Request
        const response = await fetch(url, options)

        // Alert the User there was an Error when there was not a valid response
        if(response.status !== 200 && response.status !== 201) {
            const data = await response.json()
            alert(data.message)
        } else {
            // Successful
            updateCallback()
        }
    }

    return <form onSubmit={onSubmit}>
        <div>
            <label htmlFor = "firstName">First Name:</label>
            <input
                type = "text"
                id = "firstName"
                value = {firstName}
                onChange = {(e) => setFirstName(e.target.value)}
            />
            <label htmlFor = "lastName">Last Name:</label>
            <input
                type = "text"
                id = "lastName"
                value = {lastName}
                onChange = {(e) => setLastName(e.target.value)}
            />
            <label htmlFor = "email">Email:</label>
            <input
                type = "text"
                id = "email"
                value = {email}
                onChange = {(e) => setEmail(e.target.value)}
            />
        </div>
        {/* On Submit go back to onSubmit Function */}
        <button type = "submit">Create Contact</button>
    </form>
}

// Needs to be exported in order to import
export default ContactForm