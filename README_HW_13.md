# Homework_13. Celery.

Homework for hillel IT school. 
Based on [MDN tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)
---------------------

### Tasks:

1. Add a page with a form aka `reminder` for sending email with some remind information:
   - field `email` for sending address;
   - field `text` for remind text;
   - field `datetime` for data and time for reminding;
2. When submitting a form, a task is created and postponed, 
   which will have to be completed at the time specified in the form and send a `reminder` to the specified form.
3. Date and time for reminding can't be more than 2 days in advance and can't be in the past.
4. In the subject line, you can simply specify a "reminder".
5. Use console mail sending.

---------------------
BASE_DIR: `/catalog/`

TECHNOLOGY_STACK: `Celery`, `Django`, `RabbitMQ`

---------------------

### License

GPLv3
