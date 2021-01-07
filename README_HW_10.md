# Homework_10. Django middleware.

Homework for hillel IT school. 
Based on [MDN tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)
---------------------

### Tasks:

1. Create a new model `LogModel` for logging all requests except requests to admin part.
   
   Fields:
    - `path` (CharField)
    - `method` (CharField)
    - `timestamp` (DataTimeField)

2. Create middleware `LogMiddleware` and add to the `settings.py`.
3. Create ModelAdmin for `Logmodel`.

---------------------
BASE_DIR: `/catalog/`

---------------------

### License

GPLv3
