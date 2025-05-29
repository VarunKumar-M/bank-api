🚀 Features
Load bank and branch data from CSV

SQLite + SQLAlchemy ORM integration

REST API endpoints:

GET /banks/ – List all banks

GET /branches/?ifsc=XYZ – Get branch by IFSC

GET /branches/?branch=XYZ – Search branches by name

Modular structure (routers, models, schemas)

Interactive docs at /docs (Swagger UI)

🛠 Tech Stack
Backend: FastAPI

Database: SQLite

ORM: SQLAlchemy

Language: Python 3.9+

🧠 Approach
Parsed bank_branches.csv using Python's csv module

Defined Bank and Branch models (1:N relationship)

Seeder script inserts data into SQLite

Clean API structure with dependency injection

🧪 Testing
Manual via Swagger UI

Automated using pytest

⚙️ Setup
bash
Copy
Edit
pip install -r requirements.txt
uvicorn app.main:app --reload
✅ Test
bash
Copy
Edit
pytest
⏱ Time Taken
~2.5 hours total