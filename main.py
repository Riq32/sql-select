# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# Add code below and run file to see data from employees table

employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# STEP 2
# Replace None with your code
# Select only employeeNumber and lastName from every row in employees.
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName
    FROM employees
""", conn)

# STEP 3
# Replace None with your code
# Same two columns, but lastName listed before employeeNumber.
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber
    FROM employees
""", conn)

# STEP 4
# Replace None with your code
# Alias employeeNumber as 'ID'.
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID
    FROM employees
""", conn)

# STEP 5
# Replace None with your code
# Use CASE to bin job titles into 'Executive' vs 'Not Executive'.
df_executive = pd.read_sql("""
    SELECT
        *,
        CASE
            WHEN jobTitle = 'President'
                OR jobTitle = 'VP Sales'
                OR jobTitle = 'VP Marketing'
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)

# STEP 6
# Replace None with your code
# Length of each employee's last name, returned as name_length.
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees
""", conn)


# Add the code below and run the file to see order details data

order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")


# STEP 7
# Replace None with your code
# First two characters of each employee's jobTitle, as short_title.
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
""", conn)

# STEP 8
# Replace None with your code
# Total amount for all orders: sum of rounded (priceEach * quantityOrdered).
# priceEach/quantityOrdered are stored as text, so they're cast to REAL
# before multiplying; ROUND() then rounds each order line's total before
# everything gets summed together in Python.
#
# .sum() on a one-column DataFrame returns a Series indexed by the column
# name ('total_price'), not by position. reset_index(drop=True) swaps that
# for a plain integer index so sum_total_price[0] reliably retrieves the
# value (recent pandas versions no longer fall back to positional lookup
# for Series.__getitem__).
sum_total_price = pd.read_sql("""
    SELECT ROUND(CAST(priceEach AS REAL) * CAST(quantityOrdered AS REAL)) AS total_price
    FROM orderDetails
""", conn).sum().reset_index(drop=True)

# STEP 9
# Replace None with your code
# Original orderDate plus day/month/year pulled out via SQLite's
# strftime() date function.
df_day_month_year = pd.read_sql("""
    SELECT
        orderDate,
        strftime('%d', orderDate) AS day,
        strftime('%m', orderDate) AS month,
        strftime('%Y', orderDate) AS year
    FROM orders
""", conn)


# Close the connection
conn.close()