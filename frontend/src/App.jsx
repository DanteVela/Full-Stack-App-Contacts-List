import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [contacts, setContacts] = useState([])

  useEffect(() => {
    fetchContacts()
  }, [])

  // Async Function to Fetch Contacts
  const fetchContacts = async () => {
    // fetch(): Send a Request [Usually a GET Request]
    // Flask Server: http://127.0.0.1:5000/contacts
    const response = await fetch("http://127.0.0.1:5000/contacts")

    // Get the JSON Data
    const data = await response.json()
    setContacts(data.contacts)
    
    // To see the Data
    console.log(data.contacts)
  }

  return (
    <>

    </>
  )
}

export default App
