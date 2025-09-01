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


## 4. 4. SQL vs NoSQL
