TNPG: STEVE. Roster: Ryan, Joseph, Samson 10/24/2022

DISCO: Databases don't have a file extension. sqlite shell commands use semicolons.

Creating a database: $ touch

Opening a database in sqlite: $ sqlite3

Creating a database through sqlite shell: Step 1: Run the sqlite shell by opening a database $ sqlite3 Note: If the database doesn't exist then it will access an empty database. This doesn't mean that the database is created yet.

Step 2: Create a table by typing CREATE TABLE

( , ...); Note: After creating a table in an empty database, the database file will be created.
Basics in the sqlite shell:

Creating a table: CREATE TABLE

( , ...); Ex: CREATE TABLE students (name TEXT, osis INTEGER); This creates a table with 2 columns. INSERT INTO will now only accept 2 fields because there are 2 columns.
Inserting data into a table: INSERT INTO

VALUES (<field 1>, <field 2>, ...); Note: The number of fields must match the number of columns you created. This command will create a new row with each field filling in its respective column in order. Ex: INSERT INTO students VALUES ("Ryan", 12345);

If you want to insert values into select columns: INSERT INTO

(, , ...) VALUES (<field 1>, <field 2>, ...); Note: The number of columns you want to insert values into must match the number of fields. The fields will fill in values matching the order of the columns you selected.
List out the database: SELECT , , ... FROM

Ex: SELECT name, osis FROM students

If you want to delete values from the table: DELETE FROM 

Ex: DELETE FROM students; Note: this will delete the whole table

Ex: DELETE FROM students WHERE osis = 12345; Note: this will delete all the students who have the osis 12345

If you want to update all occurances of any string or subset of it: REPLACE

(...,...,...); Ex: REPLACE("Ryan", "yan", "ay"); Note: this will turn all occurance of the string "Ryan" and replace the "yan" inside it with "ay". The result should be "Ray"