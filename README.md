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
---
## Data Flow Diagram
<a href="URL_OF_LARGE_IMAGE">
  <img src="URL_OF_SMALL_IMAGE" alt="Alt text" width="300"/>
</a>


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

## Tech Stack

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

## Project Structure

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
git clone https://github.com/DISHANK-PATEL/Django_Task_Board_API.git
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
## Sample Screenshots

<img width="1308" height="891" alt="image" src="https://github.com/user-attachments/assets/6fe8d3d4-26d4-492a-9de1-cde1b733af21" />

<img width="943" height="275" alt="image" src="https://github.com/user-attachments/assets/67148fd3-0d0d-436b-9059-ac4c61e29169" />
<img width="272" height="292" alt="image" src="https://github.com/user-attachments/assets/9d77b800-1bd9-42f8-be68-60e126097fc1" />
<img width="555" height="598" alt="image" src="https://github.com/user-attachments/assets/c58ad140-9e45-4985-a566-f0e72178c059" />
<img width="262" height="304" alt="image" src="https://github.com/user-attachments/assets/5d02b54f-98cf-43ac-95ee-4329f556f4fb" />
<img width="537" height="598" alt="image" src="https://github.com/user-attachments/assets/15d74159-adec-4129-82fe-8dddd3c16ae7" />
<img width="793" height="370" alt="image" src="https://github.com/user-attachments/assets/f734cde6-4e28-475f-a90e-b86540432ced" />
<img width="1273" height="630" alt="image" src="https://github.com/user-attachments/assets/dc1ebad9-d248-4a84-82b4-fc2119e5e0ca" />


<img width="998" height="643" alt="image" src="https://github.com/user-attachments/assets/d192dcdc-0ef4-40ea-ab95-0824068b4fdb" />
<img width="622" height="732" alt="image" src="https://github.com/user-attachments/assets/104ae87d-2fe9-48f4-8d13-576440e65d9b" />
<img width="1494" height="361" alt="image" src="https://github.com/user-attachments/assets/5e967747-df44-4ffb-ab7f-c9bdd4b9fa3e" />

<img width="1005" height="673" alt="image" src="https://github.com/user-attachments/assets/de0b9f50-0ddb-4dcb-b461-6a8b7c8db92a" />
<img width="1018" height="757" alt="image" src="https://github.com/user-attachments/assets/3a9b0d5d-b1fb-4ed7-808b-8439350a94a1" />
<img width="1892" height="782" alt="image" src="https://github.com/user-attachments/assets/df04bede-bae6-470b-849a-5fe7f48a25b9" />


---

