TNPG: STEVE. Roster: Ryan, Joseph, Samson
10/24/2022

DISCO:
Databases don't have a file extension.
sqlite shell commands use semicolons.

Creating a database:
$ touch <database name>

Opening a database in sqlite:
$ sqlite3 <database name>

Creating a database through sqlite shell:
Step 1: Run the sqlite shell by opening a database
$ sqlite3 <database name>
Note: If the database doesn't exist then it will access an empty database. This doesn't mean that the database is created yet.

Step 2: Create a table by typing
CREATE TABLE <table name> (<column name> <data type>, ...);
Note: After creating a table in an empty database, the database file will be created.

Basics in the sqlite shell:

Creating a table:
CREATE TABLE <table name> (<column name> <data type>, ...);
Ex: CREATE TABLE students (name TEXT, osis INTEGER);
This creates a table with 2 columns. INSERT INTO will now only accept 2 fields because there are 2 columns.

Inserting data into a table:
INSERT INTO <table name> VALUES (<field 1>, <field 2>, ...);
Note: The number of fields must match the number of columns you created. This command will create a new row with each field filling in its respective column in order.
Ex: INSERT INTO students VALUES ("Ryan", 12345);

If you want to insert values into select columns:
INSERT INTO <table name>(<column name>, <column name>, ...) VALUES (<field 1>, <field 2>, ...);
Note: The number of columns you want to insert values into must match the number of fields. The fields will fill in values matching the order of the columns you selected.

List out the database:
SELECT <column name>, <column name>, ... FROM <table name>
Ex: SELECT name, osis FROM students