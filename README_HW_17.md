# Homework_17. Django templates tags and filters.

Homework for hillel IT school. 
Based on [MDN tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)
---------------------

### Tasks:
Based on homework 16 'https://github.com/CapitanS/hillel_hw07_django/blob/main/README_HW_16.md'
1. Write a custom template tag.
2. Write a custom template filter.

Extra:
1. Write a custom template tag for rendering form with bootstrap style
2. Write a custom template filter for replacing forbidden words from`https://random-word-api.herokuapp.com/home`
   Cache response with forbidden words from api.

---------------------
BASE_DIR: `/orders/`

BASE_URL: `http://127.0.0.1:8000/orders/customers_price`

1. Custom templates tag: `total_price` in `poll_extras.py`
2. Custom templates filter: `currency` in `poll_extras.py`

Extra:
1. Custom templates tag: `city_form` in `poll_extras.py`
   BASE_URL: `http://127.0.0.1:8000/orders/city/create/`
2. Custom templates filter: `check_forbidden_words` in `poll_extras.py`
   BASE_URL: `http://127.0.0.1:8000/orders/customers_price`

---------------------

### License

GPLv3
