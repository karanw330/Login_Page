# 🔐 Flask Login Page with AJAX & SQLAlchemy 

This is a secure login page built using **Flask**, **SQLAlchemy**, **AJAX**, and **vanilla JavaScript**. The app validates user input on the client side, then uses AJAX to check credentials with the backend. 
Based on the server’s response, it either redirects or displays appropriate messages without reloading the page.

---

## 🚀 Features

- Username and password validation (client-side)
- Password encryption and secure database lookup
- AJAX-based communication between JavaScript and Flask
- JSON-based server responses
- Redirects to landing page on successful login
- Realtime error handling without page reload
- Custom Hashing Function – (can be changed for more security)

---

## 🛠️ Tech Stack

- **Flask** – Lightweight Python web framework  
- **SQLAlchemy** – ORM for database interaction  
- **JavaScript (Fetch API)** – Handles AJAX calls  
- **HTML/CSS** – Frontend interface (Bootstrap optional)  
- **SQLite** – Lightweight development database (can swap later)

---

✅ Note: **1)** This app uses a custom password hashing function (enc()). In production, it's recommended to use proven libraries like bcrypt or werkzeug.security to ensure cryptographic strength and salt handling.
          **2)** Don't forget to replace app.db with your actual database filename if you've named it differently.
