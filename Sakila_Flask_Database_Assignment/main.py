import os 
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jasmine9459",
    port=3306,
    database="sakila"
)

sql = """
SELECT 
    c.first_name,
    c.last_name,
    c.email,
    ci.city,
    co.country,
    c.active,
    MAX(r.rental_date) AS last_rental_date,
    MAX(f.title) AS last_rental_film
FROM 
    sakila.customer AS c
JOIN 
    sakila.address AS a ON c.address_id = a.address_id
JOIN 
    sakila.city AS ci ON a.city_id = ci.city_id
JOIN 
    sakila.country AS co ON ci.country_id = co.country_id
LEFT JOIN 
    sakila.rental AS r ON c.customer_id = r.customer_id
LEFT JOIN 
    sakila.inventory AS i ON r.inventory_id = i.inventory_id
LEFT JOIN 
    sakila.film AS f ON i.film_id = f.film_id
GROUP BY 
    c.customer_id, c.first_name, c.last_name, c.email, ci.city, co.country, c.active
ORDER BY 
    c.last_name, c.first_name;
"""
# Get Data
mycursor = mydb.cursor()
mycursor.execute(sql)
myresult = mycursor.fetchall()

# Create DataFrame
df = pd.DataFrame(myresult, columns=['First Name', 'Last Name', 'Email', 'City', 'Country', 'Active', 'Last Rental Date', 'Last Rental Film'])

# Export DataFrame to HTML
df.to_html('app/templates/customerinfo/customerinfo.html', index=False)
