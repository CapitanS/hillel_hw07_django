# Homework_7. Queryset filter, managment commands.

Homework for hillel IT school. 
Based on [MDN tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)
---------------------

### Tasks:
Write a custom manager command that will generate random users with username, email and password. 
The command takes one required argument - the number of newly generated users. 
Values less than 1 and greater than 10 should cause an error.

---------------------
BASE_DIR for management commands: `/catalog/management/commands/`

Command: `generate_users.py`

Run the following command.
```
python3 manage.py generate_users <number_of_users>
```

---------------------

### License

GPLv3
