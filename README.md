# Advanced Role-Based Access Control (RBAC) System 🚀

This project implements an **Advanced Role-Based Access Control (RBAC)** system where different user roles (Admin, Recruiter, Hiring Manager) have distinct permissions for managing **Jobs** and **Candidates**.  

The application demonstrates a **full-stack system** using **React (frontend)**, **Django + DRF (backend)**, and **MySQL (database)**. It follows industry practices with Git versioning, Swagger documentation, and clear separation of concerns.

---

## 1. Technology Stack 💻

- **Frontend**: React 19  
  - Modern, component-based UI framework  
  - React Router for navigation  
  - Axios for API calls  
- **Backend**: Django 4.2 + Django REST Framework  
  - JWT Authentication (`djangorestframework-simplejwt`)  
  - Swagger (drf-yasg) for API documentation  
- **Database**: MySQL 8+  
  - Stores Users, Jobs, Candidates with proper foreign key relationships  
- **Authentication**: JWT tokens (access + refresh) with roles embedded  

---

## 2. Project Structure 📁

Advanced-Role-Based-Access-Control/
├── backend/ # Django + DRF project
│ ├── api/ # App (models, serializers, views, permissions, urls)
│ ├── backend/ # Django project settings
│ ├── requirements.txt
│ └── .env # Database and secret config
├── frontend/ # React app
│ ├── src/
│ │ ├── pages/ # Login, Dashboard, Jobs, Candidates
│ │ ├── api.js # Axios wrapper with JWT
│ │ ├── index.css # Global styles
│ │ └── App.jsx # Router setup
└── README.md # Documentation

pgsql
Copy code

---

## 3. Setup Instructions ⚙️

### 🔹 Backend (Django + MySQL)

1. **Create MySQL Database**
sql
CREATE DATABASE rbac_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER 'rbacuser'@'%' IDENTIFIED BY 'rbacpass';
GRANT ALL ON rbac_db.* TO 'rbacuser'@'%';
FLUSH PRIVILEGES;
Install dependencies

bash
Copy code
cd backend
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
Environment variables (backend/.env)

ini
Copy code
MYSQL_DATABASE=rbac_db
MYSQL_USER=rbacuser
MYSQL_PASSWORD=rbacpass
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
DJANGO_SECRET=change-this-secret
Run migrations and create sample users

      python manage.py makemigrations
      python manage.py migrate
      python manage.py create_sample_users
      python manage.py runserver
      
👉 Swagger docs available at: http://localhost:8000/swagger/

🔹 Frontend (React)

    cd frontend
    npm install
    npm start
    
👉 React app runs at: http://localhost:3000

4. Roles & Permissions 🔑

Role	Jobs CRUD	Candidates View
Admin	Create, Read, Update, Delete	Full access
Recruiter	Create, Read, Update (No Delete)	Full access
Hiring Manager	Read-only Jobs, Assigned candidates only	Limited view

Test Users (auto-created):

Admin → admin@example.com / adminpass

Recruiter → rec1@example.com / recpass

Hiring Manager → hm1@example.com / hmpass

5. API Documentation & Testing ✅

Swagger (OpenAPI)
Fully integrated at /swagger/

Provides interactive docs for Jobs & Candidates APIs

Allows testing of endpoints with JWT authentication

Unit Testing:

Backend: Django TestCase for authentication, job creation, candidate filtering

Frontend: Component tests (Login form, Candidate form rendering)

Run tests:

# Backend
    python manage.py test

# Frontend
    npm test
    
6. Git & Code Management 📦

Separate repo for each project (this one is for RBAC).

Commit messages use conventional commits:

Example: feat: add candidate modal

Example: fix: recruiter cannot delete jobs

Push daily for backup:

    git add .
    git commit -m "feat: add edit job modal"
    git push origin master
    
Clone repo:

    git clone https://github.com/msushmithareddy26/Advanced-Role-Based-Access-Control.git
    
7. Demo Guidelines 🎯:

What: A full-stack RBAC system for Jobs & Candidates management.

How:

Show UI → Login → Dashboard → Jobs & Candidates pages.

Show role-based differences (Admin can delete jobs, Recruiter cannot).

Show backend API in Swagger and how JWT is used.

Run unit tests to prove correctness.

Why:

Django chosen for robust backend and built-in auth.

React for modern, responsive UI with role-aware rendering.

MySQL for relational data integrity.

JWT for industry-standard authentication.

Swagger for professional API documentation.

8. Future Improvements 🚀:

Audit logs for all CRUD actions

Docker Compose setup for one-click deployment

CI/CD pipeline with GitHub Actions

Deployment on cloud (Heroku / Render / Vercel)

📜 License
MIT License
