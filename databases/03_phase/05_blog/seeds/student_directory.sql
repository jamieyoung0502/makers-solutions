DROP TABLE IF EXISTS cohorts CASCADE;
DROP SEQUENCE IF EXISTS cohorts_id_seq;
DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;

CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date date
);

INSERT INTO cohorts (name, starting_date) VALUES ('April', '04/01/2023');

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO students (name, cohort_id) VALUES ('Adrian', 1);
INSERT INTO students (name, cohort_id) VALUES ('Nish', 1);
INSERT INTO students (name, cohort_id) VALUES ('Jasmine', 1);
INSERT INTO students (name, cohort_id) VALUES ('Saamiya', 1);



