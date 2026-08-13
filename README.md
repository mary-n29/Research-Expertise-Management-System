# Research & Expertise Management System

## CS 5614 – Individual Database Project

**Course:** CS 5614 – Database Management Systems  
**Semester:** Summer II 2026  
**Database Management System:** MySQL 8.0  
**Programming Language:** Python 3.x  
**GUI Framework:** Tkinter  

---

# Project Overview

The Research & Expertise Management System is a desktop database application developed to manage information related to university research activities. The system enables administrators to maintain records for researchers, research projects, publications, sponsors, and the relationships between them.

The application provides an intuitive graphical user interface (GUI) that allows users to interact with the database without writing SQL queries.

The project demonstrates relational database design principles, database normalization, referential integrity, SQL programming, and application development using Python and MySQL.

---

# Features

The application currently supports:

### Researcher Management
- Add researchers
- Update researcher information
- Delete researchers
- Search researchers
- View all researchers

### Project Management
- Add projects
- Update projects
- Delete projects
- Search projects
- View all projects

### Publication Management
- Add publications
- Update publications
- Delete publications
- Search publications
- View all publications

### Relationship Management
- Assign researchers to projects
- Assign researchers as publication authors
- View existing assignments

### Reporting
- Database statistics dashboard
- Researcher statistics
- Department summaries
- Position summaries
- Aggregate SQL reports

---

# Database Schema

The database is named:

`ResearchExpertiseDB`

The schema contains the following tables:

- SPONSOR
- PROJECT
- DELIVERABLE
- RESEARCHER
- PROJECT_MEMBERSHIP
- SKILL
- RESEARCHER_SKILL
- PUBLICATION
- PUBLICATION_AUTHOR
- RESEARCH_AREA

Associative tables are used to represent many-to-many relationships between researchers, projects, publications, and skills.

---

# Database Constraints

The database enforces data integrity using:

- Primary Keys
- Composite Primary Keys
- Foreign Keys
- NOT NULL Constraints
- UNIQUE Constraints
- CHECK Constraints
- Referential Integrity

Examples include:

- Non-negative project funding
- Valid project dates
- Valid deliverable status values
- Valid researcher proficiency levels

---

# Technologies Used

- Python 3
- Tkinter
- MySQL 8
- MySQL Connector/Python

---

# Project Structure

```text
Research-Expertise-Management-System/

│
├── README.md
├── ID.txt
├── main.py
├── db_connection.py
├── main_menu.py
├── researcher.py
├── project.py
├── publication.py
├── relationship_management.py
├── reports.py
│
├── sql/
│   ├── create_database.sql
│   ├── create_tables.sql
│   └── sample_data.sql
│
└── screenshots/
```

---

# Installation

## Prerequisites

Install:

- Python 3.x
- MySQL Server 8.x
- MySQL Workbench (recommended)

Install the required Python package:

```bash
pip install mysql-connector-python
```

---

# Database Setup

1. Open MySQL Workbench.

2. Execute:

```
create_database.sql
```

3. Execute:

```
create_tables.sql
```

4. Execute:

```
sample_data.sql
```

5. Verify the database name is:

```
ResearchExpertiseDB
```

---

# Configure the Database Connection

Update `db_connection.py` with your MySQL credentials.

Example:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="ResearchExpertiseDB"
)
```

---

# Running the Application

Run:

```bash
python main.py
```

The application opens with the database connection screen.

After connecting successfully, users can access the main dashboard.

---

# Main Application Modules

- Dashboard
- Researcher Management
- Project Management
- Publication Management
- Relationship Management
- Reports & Statistics

---

# SQL Features Demonstrated

The project demonstrates:

- INSERT
- UPDATE
- DELETE
- SELECT
- INNER JOIN
- LEFT JOIN
- GROUP BY
- ORDER BY
- Aggregate Functions
    - COUNT
    - SUM
    - AVG
    - MAX

---

# Database Relationships

The system manages several many-to-many relationships, including:

- Researchers ↔ Projects
- Researchers ↔ Publications
- Researchers ↔ Skills

These relationships are implemented using associative tables.

---

# Future Enhancements

Potential improvements include:

- User authentication and role-based access
- Research area management interface
- Deliverable management interface
- Data visualization with charts
- Export reports to PDF or Excel
- Email notifications for project deadlines

---

# Author

**Mary Nerayo**

Virginia Tech

CS 5614 – Summer II 2026