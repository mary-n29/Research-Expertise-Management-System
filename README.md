<<<<<<< HEAD
# Research & Expertise Management System

## CS 5614 Database Project

**DBMS:** MySQL 8.0  
**Interface Language:** Python  

---

## Project Overview

The Research & Expertise Management System is a database project designed to manage information related to researchers, research projects, sponsors, skills, publications, research areas, and project deliverables.

The system provides a structured relational database for storing research management information and representing relationships such as researcher participation in projects, researcher skills, and publication authorship.

The database was designed using relational database design principles, including normalization, primary and foreign key constraints, referential integrity, and other database constraints.

---

## Database Schema

The database is named:

`ResearchExpertiseDB`

The database contains the following tables:

- `SPONSOR`
- `PROJECT`
- `DELIVERABLE`
- `RESEARCHER`
- `PROJECT_MEMBERSHIP`
- `SKILL`
- `RESEARCHER_SKILL`
- `PUBLICATION`
- `PUBLICATION_AUTHOR`
- `RESEARCH_AREA`

Associative tables are used to represent many-to-many relationships where appropriate.

---

## Database Constraints

The schema uses database constraints to maintain data integrity, including:

- Primary keys
- Composite primary keys
- Foreign keys
- `NOT NULL` constraints
- `UNIQUE` constraints
- `CHECK` constraints
- Referential integrity constraints

Examples include validation of project funding amounts, project dates, deliverable statuses, and researcher skill proficiency levels.

---

## Python Database Interface

A simple Python interface is included to demonstrate connectivity between the application layer and the MySQL database.

The interface was implemented using:

- Python
- Tkinter
- MySQL Connector/Python

---

## Project Structure

```text
Research-Expertise-Management-System/
│
├── README.md
├── ID.txt
│
├── sql/
│   ├── create_db.sql
│   ├── create_tables.sql
│   └── research_db_sample_data.sql
│
└── db_connection.py
=======
# Research-Expertise-Management-System
>>>>>>> 24f100da7b04c35e27be15b2267e5345b517196b
