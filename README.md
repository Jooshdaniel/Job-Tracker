# Job Application Tracker (Deployed Backend API)

A backend service for tracking job applications, their statuses, and notes through a RESTful API.
This project demonstrates end-to-end backend development including API design, database integration, and cloud deployment.
https://job-tracker-1-v1i9.onrender.com/docs
---

## Features

* Create job applications with company, position, status, and notes
* Retrieve all stored job applications
* Update application status
* Delete job applications
* Persistent storage using a relational database
* Automatic API documentation via Swagger UI
* Deployed to a cloud hosting platform

---

## Tech Stack

* Language: Python
* Framework: FastAPI
* Database: SQLite (SQLAlchemy ORM)
* Server: Uvicorn
* Deployment: Render
* Version Control: Git and GitHub

---

## Project Structure

```
job-tracker/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── jobs.py
│   ├── models/
│   │   └── job.py
│   └── db/
│       └── database.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/job-tracker.git
cd job-tracker
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m uvicorn app.main:app --reload
```

### 5. Open API documentation

Navigate to:

```
http://127.0.0.1:8000/docs
```

---

## Deployment

The application is deployed using Render with automated builds from GitHub.

Start command used in deployment:

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT
```


