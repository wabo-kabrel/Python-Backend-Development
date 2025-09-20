# Databases in Flask
## 1. What is a Database?
- A **database** stores your app's data in an **organized** way.
- Your Flask app **queries** the database to read/write information.
- Two main types:
  - **SQL (Relational)** → Structured, uses tables, rows, columns, supports joins.
  - **NoSQL (Non-relational)** → Flexible, uses documents, collections, often faster for large-scale unstructured data.

## 2. SQL Databases (Relational)
- **Core idea:** Stores data in **tables** (like spread).
- **Tables:**
  - **Columns** = **attributes** (e.g., name, email, password).
  - **Rows** = actual **records**.
  
- **Keys**:
  - **Primary Key (PK)** = unique **ID** for each row.
  - **Foreign Key (FK)** = link between tables.

- **Relationships:**
  - **One-to-Many** → e.g., one role can belong to many users.
  - **Many-to-Many** → e.g., users can enroll in many courses.
  - Joins are used to combine data across tables.

**Example (user & roles):**
| roles | users                              |
| ----- | ---------------------------------- |
| id=1  | id=101, username=john, role\_id=1  |
| id=2  | id=102, username=susan, role\_id=2 |

- `users.role_id` → references `roles.id`.
  
👉 Efficient, no data duplication, but sometimes complex queries.

## 3. NoSQL Databases
- **NoSQL** = "Not Only SQL".
- Data stored as:
  - **Documents** (JSON-like objects).
  - **Collections** (group of documents). 
- No joins. Instead, **denormalization** is common → store repeated data for speed.
- Example: Instead of separate `users` & `roles`, store role info inside each user document:
```json
{
  "id": 101,
  "username": "john",
  "role": { "id": 1, "name": "Admin" }
}
```

👉 Pros: Faster reads (no joins).  
👉 Cons: Updating role = update every user’s document.  


## 4. SQL vs NoSQL

| Feature          | SQL (Relational)            | NoSQL (Document)              |
| ---------------- | --------------------------- | ----------------------------- |
| Structure        | Tables, Rows, Columns       | JSON-like Documents           |
| Relationships    | Strong (joins supported)    | Weak (joins avoided)          |
| Data Duplication | Low                         | High (due to denormalization) |
| Best For         | Structured, consistent data | Flexible, fast reads          |

✅ For **Flask apps** (especially small/medium projects) → SQL is usually the better choice.


## 5. Flask and Databases
Flask is **database-agnostic**:
- You can use **MySQL, PostgreSQL, SQLite, MongoDB, Redis, etc.**
- But you need a **driver** or **ORM** to connect.


## 6. SQLAlchemy (ORM for Flask)
- **ORM** = Object Relational Mapper.
- Maps Python **classes** → **database tables.**
- Example: Instead of writing SQL:
```sql
  SELECT * FROM users WHERE username='john';
```
You write Python:
```python
User.query.filter_by(username="john").first()
```

### Flask-SQLAlchemy
- Extension that integrates **SQLAlchemy** with Flask.
- Features:
  - Easy via `app.config`.
  - Provides `db` object for models & queries.
  - Supports multiple databases (SQLite, MySQL, Postgres).


## 7. Configuring Flask-SQLAlchemy

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
```
- `db.Column` → defines fields.
- `db.ForeignKey` → relationship link.
- `db.relationship` → high-level Python relationship.


## 9. Creating Tables
In a Python shell:
```python
from app import db
db.create_all()   # creates tables from models
```


## 10. CRUD Operations
**Insert**
```python
admin_role = Role(name="Admin")
user_john = User(username="john", role=admin_role)
db.session.add_all([admin_role, user_john])
db.session.commit()
```

**Query**
```python
Role.query.all()
User.query.filter_by(username="john").first()
```

**Update**
```python
admin_role.name = "Administrator"
db.session.commit()
```

**Delete**
```python
db.session.delete(admin_role)
db.session.commit()
```


## 11. Relationships
- **One-to-Many:** One role → many users.
- **Many-to-Many:** Needs an **association table**.

Example query:
```python
role = Role.query.filter_by(name="Admin").first()
print(role.users)  # list of users with Admin role
```


## 12. Database Migrations (Flask-Migrate)
- Problem: `db.create_all()` won't update when models change.
- Solution: **Migrations** (track schema changes over time).
- Tool: `Flask-Migrate` (wrapper around Alembic).

**Setup**
```bash
pip install flask-migrate
```

**In app:**
```python
from flask_migrate import Migrate
migrate = Migrate(app, db)
```

**Commands**
```bash
flask db init        # create migrations folder
flask db migrate -m "Initial migration"
flask db upgrade     # apply migration to DB
```



