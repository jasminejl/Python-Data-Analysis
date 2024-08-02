USE Sakila;

SELECT 
    c.first_name,
    c.last_name,
    c.email,
    ci.city,
    co.country,
    c.active,
    r.rental_date AS last_rental_date,
    f.title AS last_rental_film
FROM 
    customer AS c
JOIN 
    address AS a ON c.address_id = a.address_id
JOIN 
    city AS ci ON a.city_id = ci.city_id
JOIN 
    country AS co ON ci.country_id = co.country_id
LEFT JOIN 
    rental AS r ON c.customer_id = r.customer_id
LEFT JOIN 
    inventory AS i ON r.inventory_id = i.inventory_id
LEFT JOIN 
    film AS f ON i.film_id = f.film_id
ORDER BY 
    c.last_name, c.first_name;
    








