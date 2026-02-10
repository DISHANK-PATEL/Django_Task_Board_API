# Django Task Board API

A structured REST API for managing internship tasks within a team, built using **Django** and **Django REST Framework**.
This project demonstrates secure authentication, task assignment workflows, permissions enforcement, dashboard aggregation, and automated testing using industry-standard backend practices.

---

##  Overview

This backend service enables users to:

* Register and authenticate securely
* Create and manage tasks
* Assign tasks across users
* Track task progress
* View dashboard summaries
* Enforce role-based permissions

The project follows modular Django architecture with clean separation between domain logic, serialization, permissions, and API layers.

---

## Implemented Features

### Authentication

* Custom Email-based User Model
* User Registration Endpoint
* JWT Authentication (`SimpleJWT`)
* Token-based stateless authorization
* Swagger-documented endpoints

---

### Task Management

* Create Tasks
* List User-relevant Tasks
* Retrieve Task by ID
* Update Task
* Delete Task
* Assign Tasks via Email
* Status tracking (`TODO`, `DOING`, `DONE`)

---

### Permissions & Access Rules

* Creator has full control
* Only creator can delete
* Assignee restricted to status updates
* Protection against cross-user data access

---

### Dashboard Analytics

* Endpoint grouping tasks by status
* Efficient database aggregation
* Returns summarized task distribution

Example:

```json
{
  "TODO": 3,
  "DOING": 2,
  "DONE": 5
}
```

---

### Testing

* Model Tests
* API Tests
* Authenticated request testing

---

## 🛠 Tech Stack

| Layer     | Technology            |
| --------- | --------------------- |
| Language  | Python 3.12           |
| Framework | Django                |
| API       | Django REST Framework |
| Auth      | SimpleJWT             |
| Docs      | drf-spectacular       |
| DB        | SQLite                |
| Testing   | Django Test Framework |

---

## 📁 Project Structure

```
Django_Task_Board_API/
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── asgi/wsgi
│
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests/
│
├── tasks/
│   ├── models.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── views.py
│   ├── urls.py
│   └── tests/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1️ Clone Repository

```bash
git clone <repo-url>
cd Django_Task_Board_API
```

---

### 2️ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️ Apply Migrations

```bash
python manage.py migrate
```

---

### 5️ Run Server

```bash
python manage.py runserver
```

---

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/api/docs/
```

Schema:

```
http://127.0.0.1:8000/api/schema/
```

---

## API Endpoints

### Users

| Method | Endpoint               |
| ------ | ---------------------- |
| POST   | `/api/users/register/` |
| POST   | `/api/users/token/`    |
| GET    | `/users/me/tasks/`     |

---

### Tasks

| Method | Endpoint                |
| ------ | ----------------------- |
| GET    | `/api/tasks/`           |
| POST   | `/api/tasks/`           |
| GET    | `/api/tasks/{id}/`      |
| PUT    | `/api/tasks/{id}/`      |
| PATCH  | `/api/tasks/{id}/`      |
| DELETE | `/api/tasks/{id}/`      |
| GET    | `/api/tasks/dashboard/` |

---

## Running Tests

```bash
python manage.py test
```

---

## Learning Objectives Demonstrated

* Custom authentication modeling
* JWT integration
* Serializer-driven validation
* Object-level permissions
* Query scoping
* Aggregation endpoints
* Modular Django architecture
* API documentation practices

---

