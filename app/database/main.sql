-- create tables
DROP TABLE IF EXISTS employee;
CREATE TABLE employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    dob DATE NOT NULL,
    nationality TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    parent_id INTEGER
);
DROP TABLE IF EXISTS location;
CREATE TABLE location (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER NOT NULL,
    street TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip INTEGER NOT NULL,
    UNIQUE (number, street, zip)
);
DROP TABLE IF EXISTS department;
CREATE TABLE department (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id INTEGER NOT NULL,
    name TEXT NOT NULL UNIQUE,
    parent_id INTEGER
);
DROP TABLE IF EXISTS employment;
CREATE TABLE employment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    department_id INTEGER NOT NULL,
    salary FLOAT,
    effective_date DATE NOT NULL
);

-- add static data
insert into location (number, street, city, state, zip) values (234, 'Main St', 'Saratoga Springs', 'NY', '12866');
insert into department (location_id, name) values (1, 'research')