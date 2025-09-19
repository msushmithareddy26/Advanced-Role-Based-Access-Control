# Advanced Role-Based Access Control (RBAC) System 🚀

A full-stack web application implementing **Advanced Role-Based Access Control (RBAC)** for managing **Jobs** and **Candidates** across three distinct user roles: **Admin**, **Recruiter**, and **Hiring Manager**.

Built with a modern tech stack and professional-grade architecture, this project showcases secure authentication, role-aware UI rendering, and scalable backend design.

---

## 🛠️ Tech Stack Overview

| Layer       | Technology                          | Highlights                                      |
|------------|--------------------------------------|-------------------------------------------------|
| Frontend   | **React 19**                         | Component-based UI, React Router, Axios         |
| Backend    | **Django 4.2 + DRF**                 | JWT auth, role-based permissions, Swagger docs  |
| Database   | **MySQL 8+**                         | Relational integrity with FK constraints        |
| Auth       | **JWT (access + refresh)**           | Role embedded tokens for secure access          |
| Docs       | **Swagger (drf-yasg)**               | Interactive API testing and documentation       |

---

## 📁 Project Structure

Advanced-Role-Based-Access-Control/ ├── backend/ │ ├── api/ # Models, views, serializers, permissions │ ├── backend/ # Django settings │ ├── requirements.txt │ └── .env # Secrets and DB config ├── frontend/ │ ├── src/ │ │ ├── pages/ # Login, Dashboard, Jobs, Candidates │ │ ├── api.js # Axios wrapper with JWT │ │ └── App.jsx # Routing setup └── README.md # Project documentation

Code:

## ⚙️ Setup Instructions

### 🔸 Backend (Django + MySQL):

    sql
    CREATE DATABASE rbac_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
    CREATE USER 'rbacuser'@'%' IDENTIFIED BY 'rbacpass';
    GRANT ALL ON rbac_db.* TO 'rbacuser'@'%';
    FLUSH PRIVILEGES;

    cd backend
    python -m venv .venv
    source .venv/bin/activate  # or .venv\Scripts\activate (Windows)
    pip install -r requirements.txt
    
.env configuration:

    ini
    MYSQL_DATABASE=rbac_db
    MYSQL_USER=rbacuser
    MYSQL_PASSWORD=rbacpass
    MYSQL_HOST=127.0.0.1
    MYSQL_PORT=3306
    DJANGO_SECRET=change-this-secret
    Run migrations and seed users:


    python manage.py makemigrations
    python manage.py migrate
    python manage.py create_sample_users
    python manage.py runserver
    🔗 Swagger Docs: http://localhost:8000/swagger

🔸 Frontend (React):

    cd frontend
    npm install
    npm start
    🔗 React App: http://localhost:3000

🔐 Roles & Permissions Matrix:

-Role	Jobs Access	Candidates Access

-Admin	Create, Read, Update, Delete	Full access

-Recruiter	Create, Read, Update (No Delete)	Full access

-Hiring Manager	Read-only	Assigned candidates only

✅ Sample Users:

Admin: admin@example.com / adminpass

Recruiter: rec1@example.com / recpass

Hiring Manager: hm1@example.com / hmpass

📑 API Documentation & Testing:

Swagger UI: Fully integrated for Jobs & Candidates APIs

JWT Authentication: Test endpoints with role-specific tokens

Unit Tests:

Backend: TestCase for auth, job creation, candidate filtering

Frontend: Component rendering (Login, CandidateForm)


# Backend
    python manage.py test

# Frontend
    npm test
Git:
   git clone https://github.com/msushmithareddy26/Advanced-Role-Based-Access-Control.git
   
📸 Screenshots:

![WhatsApp Image 2025-09-19 at 14 42 20_0c137911](https://github.com/user-attachments/assets/1d9de6c5-68c4-43c2-9bf9-13dd76c9aca5)

![WhatsApp Image 2025-09-19 at 14 38 25_45213e93](https://github.com/user-attachments/assets/05f00b4e-a171-42db-b442-24a40c393ac3)

![WhatsApp Image 2025-09-19 at 14 57 41_592b4f66](https://github.com/user-attachments/assets/a4f349a1-089e-4be0-aa9a-17939dde0e7a)

UI walkthroughs and role-based views:

-Login & Dashboard

-Jobs CRUD by role

-Candidate filtering and assignment

🎯 Features:

*What: A secure, scalable RBAC system for job and candidate management How:

*Login → Dashboard → Jobs & Candidates

*Role-based UI behavior

*Swagger API testing with JWT

*Run unit tests to validate logic Why:

*Django for robust backend and built-in auth

*React for dynamic, role-aware UI

*MySQL for relational integrity

*JWT for secure, stateless auth

*Swagger for professional API docs

🚀 Future Enhancements:

-Audit logs for CRUD actions

-Docker Compose for one-click setup

-CI/CD with GitHub Actions

-Cloud deployment (Heroku / Render / Vercel)


📜 License
MIT License
