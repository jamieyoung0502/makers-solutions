# Single Table Design Recipe Template

_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.
```

```
Nouns:

coach, student, name, cohort
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record  | Properties   |
| ------- | ------------ |
| coach   |              |
| student | name, cohort |

Name of the table (always plural): `coaches`
Name of the table (always plural): `students`
Column names: `first_name`, `last_name` `cohort`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# COACHES:

id: SERIAL PRIMARY KEY

# STUDENTS:

id: SERIAL PRIMARY KEY
first_name: text
last_name: text
cohort: text
coach_id: SERIAL FOREIGN KEY
```

## 4. Write the SQL

```sql
-- file: coaches_table.sql
CREATE TABLE coaches (
  id SERIAL PRIMARY KEY,
);

-- file: students_table.sql

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  coach_id INTEGER,
  FOREIGN KEY (coach_id) REFERENCES coaches(id),
  first_name text,
  last_name text,
  release_year int
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < coaches_table.sql
psql -h 127.0.0.1 database_name < students_table.sql
```
