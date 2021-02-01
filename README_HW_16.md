# Homework_16. Django redis cache, templates tags and filters.

Homework for hillel IT school. 
Based on [MDN tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)
---------------------

### Tasks:
Based on homework 15 'https://github.com/CapitanS/hillel_hw07_django/blob/main/README_HW_15.md'
1. Write a custom manager command that will generate fixtures for Custom, Product, City models from homework 15
2. Create a template for pages which display fields (using aggregation/annotation):
   - first name of the customer;
   - last name of the customer;
   - order price of the customer.
3. Implement pagination on the page for many elements (100-1000).
4. Add caching to this page.
5. Use `silk` for control response time before the cache of page and after.

---------------------
BASE_DIR: `/orders/`

BASE_URL `http://127.0.0.1:8000/orders/customers_price`

BASE_DIR for management commands: `/orders/management/commands/`

Command: `generate_orders.py`

Run the following command.
```
python3 manage.py generate_orders <number_of_customers>
```

---------------------

### License

GPLv3
