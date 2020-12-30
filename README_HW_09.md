# Homework_9. Django model form.

Homework for hillel IT school. 
Based on [MDN tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)
---------------------

### Tasks:

1. Create a new model Person with fields:
    - first_name (CharField)
    - last_name (CharField)
    - email (EmailField)

2. Create modelform, view, template for creating a new record, and for editing an existing record.

---------------------
BASE_DIR: `/catalog/`

TEMPLATES_DIR: `/templates/`

URLS: 
  `/person - GET` - get the form
  `/person - POST` - validate and save the new Person object to the database
  `/person/<id: int> - GET` - get a form with Person data, or 404 if a user with this id does not exist
  `/person/<id: int> - POST` - pdate Person data, or 404

---------------------

### License

GPLv3
