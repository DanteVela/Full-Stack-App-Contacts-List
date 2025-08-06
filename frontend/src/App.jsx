import { useState, useEffect } from "react";
import ContactList from "./ContactList";
import "./App.css";
import ContactForm from "./ContactForm";

// Local:   http://localhost:5173/
// To Test: useState([{"firstName": "Tim", "lastName": "Bob", "email": "email", id: 1}])

function App() {
  const [contacts, setContacts] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [currentContact, setCurrentContact] = useState({})

  useEffect(() => {
    fetchContacts()
  }, []);

  // Async Function to Fetch Contacts
  const fetchContacts = async () => {
    // fetch(): Send a Request [Usually a GET Request]
    // Flask Server: http://127.0.0.1:5000/contacts
    const response = await fetch("http://127.0.0.1:5000/contacts");

    // Get the JSON Data
    const data = await response.json();
    setContacts(data.contacts);

    // To see the Data
    // console.log(data.contacts)
  };

  // Close Modal Function
  const closeModal = () => {
    // Close the Modal
    setIsModalOpen(false)

    // Set current contact to empty object
    setCurrentContact({})
  }

  // Open Modal Function when Creating or Editing a Contact
  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpen(true)
  }

  // Edit Modal Function
  const openEditModal = (contact) => {
    // If its open, then return
    if (isModalOpen) return

    // Otherwise set the current contact
    setCurrentContact(contact)

    // Open the Modal
    setIsModalOpen(true)
  }

  const onUpdate = () => {
    // Close Modal
    closeModal()

    // Fetch again in case of contact update
    fetchContacts()
  }

  return (
    <>
      <ContactList contacts={contacts} updateContact={openEditModal} updateCallback={onUpdate} />
      <button onClick={openCreateModal}>Create New Contact</button>
      {isModalOpen && <div className="modal">
        <div className="modal-content">
          <span className="close" onClick={closeModal}>&times;</span>
          <ContactForm existingContact={currentContact} updateCallback={onUpdate} />
        </div>
      </div>
      }
    </>
  );
}

export default App;