# Elevate labs task 5

## DELIVERABLES -

### Note:-
I created and configured a PostgreSQL database on Azure. I learned how to create users, assign roles, set database ownership, and manage privileges. I also understood the use of default tablespaces and the azure_pg_admin role in Azure-managed PostgreSQL.

### SCREENSHOTS:
<br />
Successful Deployment:
<img width="1920" height="1080" alt="deployed" src="https://github.com/user-attachments/assets/6cf0ebfd-2bb3-4381-9d6c-9de8626fa384" />

<br />
Succesful Connection from Dbeaver:
<img width="1920" height="1080" alt="connected" src="https://github.com/user-attachments/assets/b9bb82f9-a8c5-4db1-9745-5002fb6358d1" />

<br />
Table creation using SQL:
<img width="1920" height="1080" alt="table" src="https://github.com/user-attachments/assets/e3d40105-31b8-4836-aaa7-bc03b608c7b3" />

<br />
Connecting using python:
<img width="1920" height="1080" alt="python" src="https://github.com/user-attachments/assets/9f2eff92-342a-47c9-92e8-9aa60f354d6c" />
<br />
SQL Commands Used:
<br />

```sql
CREATE DATABASE intern_demo
    WITH OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    TABLESPACE = pg_default;
```

```sql
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  domain VARCHAR(30),
  score INT
);
```

```sql
INSERT INTO students (name, domain, score)
VALUES
  ('Aarav', 'Cloud', 95),
  ('Diya', 'DevOps', 89);
```

```sql
SELECT * FROM students;
```
