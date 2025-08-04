-- Query 1 : Revenue Question

SELECT 
	country,
	payment_date,
	SUM(amount) as sumCountryAmount
FROM 
	Customer
JOIN Address 
	ON Address.address_id = Customer.address_id
JOIN City 
	ON City.city_id = Address.city_id
JOIN Country 
	ON Country.country_id = City.country_id
JOIN Payment 
	ON Payment.customer_id = Customer.customer_id
AND 
	active = 1
GROUP BY 
	country, payment_date
ORDER BY 
	sumCountryAmount DESC
LIMIT
	4;
	
-- Query 2: Sentiment Question

SELECT 
	title AS MovieName, 
	description AS MovieDescription 
FROM 
	Film;
	
-- Query 3 : Country-Wise Movie-Revenue:

SELECT 
	country,
	SUM(amount) as sumCountryAmount
FROM 
	Customer
JOIN Address 
	ON Address.address_id = Customer.address_id
JOIN City 
	ON City.city_id = Address.city_id
JOIN Country 
	ON Country.country_id = City.country_id
JOIN Payment 
	ON Payment.customer_id = Customer.customer_id
AND 
	active = 1
GROUP BY 
	country
ORDER BY 
	sumCountryAmount DESC;

-- Query 4 : Revenue by Actor

SELECT 
	first_name, last_name,
	SUM(rental_rate) AS sumFilmRental
FROM 
	ACTOR
JOIN 
	FILM_ACTOR ON ACTOR.actor_id = FILM_ACTOR.actor_id
JOIN
	film ON film.film_id = FILM_ACTOR.film_id
GROUP BY 
	first_name, last_name, ACTOR.actor_id
ORDER BY 
	sumFilmRental DESC
LIMIT 
	10;
	
-- Query 5: Country Classification

SELECT 
	country,
	COUNT (DISTINCT Customer.customer_id) as cntCountryCustomers,
	(
		CASE
			WHEN COUNT (DISTINCT Customer.customer_id) >= 50 THEN 'Platinum-Class'
			WHEN COUNT (DISTINCT Customer.customer_id) BETWEEN 30 AND 49 THEN 'Gold-Class'
			WHEN COUNT (DISTINCT Customer.customer_id) BETWEEN 20 AND 29 THEN 'Silver-Class'
			ELSE 'Bronze-Class'
		END
	) AS CustomerCountryCategory
FROM 
	Customer
JOIN Address 
	ON Address.address_id = Customer.address_id
JOIN City 
	ON City.city_id = Address.city_id
JOIN Country 
	ON Country.country_id = City.country_id
JOIN Payment 
	ON Payment.customer_id = Customer.customer_id
AND 
	active = 1
GROUP BY 
	country
ORDER BY 
	cntCountryCustomers DESC
LIMIT 20;

-- Final Query:

SELECT 
	country,
	COUNT (DISTINCT Customer.customer_id) as cntCountryCustomers
FROM 
	Customer
JOIN Address 
	ON Address.address_id = Customer.address_id
JOIN City 
	ON City.city_id = Address.city_id
JOIN Country 
	ON Country.country_id = City.country_id
JOIN Payment 
	ON Payment.customer_id = Customer.customer_id
AND 
	active = 1
GROUP BY 
	country
ORDER BY 
	cntCountryCustomers DESC
LIMIT 
	20;