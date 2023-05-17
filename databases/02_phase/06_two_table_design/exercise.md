# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.
```

```
Nouns:

student, cohort, start_date, cohort_name, student_name
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record  | Properties       |
| ------- | ---------------- |
| student | name             |
| cohort  | start_date, name |

1. Name of the first table (always plural): `students`

   Column names: `name`

2. Name of the second table (always plural): `cohorts`

   Column names: `start_date`, `name`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: students
id: SERIAL
name: text

Table: cohorts
id: SERIAL
start_date: date
name: text
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one [student] have many [cohorts]? (No)
2. Can one [cohort] have many [students]? (Yes)

You'll then be able to say that:

1. **[cohort] has many [students]**
2. And on the other side, **[student] belongs to [cohort]**
3. In that case, the foreign key is in the table [students]

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one student have many cohorts? NO
2. Can one cohort have many students? YES

-> Therefore,
-> A cohort HAS MANY students
-> A student BELONGS TO a cohort

-> Therefore, the foreign key is on the students table.
```

_If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table)._

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: students_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  start_date date,
  name text,
);

-- Then the table with the foreign key second.
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
-- The foreign key name is always {other_table_singular}_id
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id)
    references cohort(id)
    on delete cascade
);

```

## 5. Create the tables

```bash
psql -h 127.0.0.1 school < students_table.sql
```
