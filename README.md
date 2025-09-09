# 🐍 Python Web Applications Portfolio

A growing collection of **Python-powered web applications** demonstrating modern full-stack web development using frameworks like **Flask**, **FastAPI**, **Django**, and more.

This repository is intended as a **portfolio** of diverse web projects — each one focusing on different skills, technologies, and concepts in web development using Python.  
At present, the portfolio contains:

- ✅ **1. deployed application**  
- 🚧 More applications **coming soon**

---

## 📂 Table of Contents
1. [About This Repository](#about-this-repository)
2. [Applications](#applications)
    - [E-Commerce Marketplace](#1-e-commerce-marketplace)
    - [Yet to Come](#yet-to-come)
3. [Technologies Used](#technologies-used)
4. [How to Run Locally](#how-to-run-locally)
5. [Planned Future Applications](#planned-future-applications)
6. [Contributing](#contributing)
7. [License](#license)

---

## 📜 About This Repository

This portfolio showcases **functional, real-world Python applications** that can be deployed and scaled for actual usage.  
The applications demonstrate:

- **Backend frameworks** (e.g., Flask, SQLAlchemy, possibly FastAPI/Django in the future)
- **Relational databases**, ORM integration
- **Deployable architectures**
- **REST API design**
- Secure authentication/authorization
- Dynamic HTML templating with Jinja2 (for Flask projects)

---


## 🚀 Applications

### **1. E-Commerce Marketplace**

**Description:**  
A fully functional e-commerce platform where users can **buy and sell products**, manage inventory, and make secure purchases online.  
The marketplace allows a variety of categories, user authentication, product listings, a shopping cart system, and basic order management.

**Key Features:**
- User registration & login system
- Product listing with images and descriptions
- Role-based access (buyer/seller capabilities)
- Shopping cart holding purchase history
- SQLAlchemy ORM-based relational database
- Secure database creation and appropriate validations
- Flask-based backend serving dynamic content

**Tech Stack:**
- **Backend:** Flask (Python)
- **Database:** SQLite3 (Main) / PostgreSQL (configurable) / MySQL
- **ORM:** SQLAlchemy
- **Frontend:** HTML5, CSS, Bootstrap

---


### **Yet to Come**

Future applications will be added here:

| Application Name | Description       | Status |
|------------------|-------------------|--------|
| Fitness tracker  | Streamlit? Flask? | YTS... |

- **Will add in due time.**

---


## 🛠️ Technologies Used

- **Python 3.x**
- **Flask** – Micro web framework
- **SQLAlchemy** – ORM for database management
- **Bootstrap & CSS** – Frontend styling
- **Javascript** - For some custom functionality
- **SQLite / PostgreSQL** – Databases
- **Jinja2** – HTML templating
- **WTForms** (optional) – Server-side form handling
- **Git & GitHub** – Version control and hosting

---


## 💻 How to Run Locally

1. **Clone the repository**
- git clone  https://github.com/varishtraheja/python-web-based-apps.git
- cd python-web-based-apps/web-app-1


2. **Create a virtual environment**
- python -m venv venv
- source venv/bin/activate # Mac/Linux
- venv\Scripts\activate # Windows


3. **Install dependencies**
pip install -r requirements.txt


4. **Set environment variables (example for Flask)**
export FLASK_APP=main.py
export FLASK_ENV=development


5. **Initialize the database**
flask db init

---

App runs at: [**http://127.0.0.1:5000/**](http://127.0.0.1:5000/)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork this repository and submit a pull request.

---

## 📄 License
This project is licensed under the **MIT License** — you’re free to use, modify, and distribute this code with attribution.

---

> **Note:** This repository will expand over time as I build more Python-based web applications. Stay tuned for updates!