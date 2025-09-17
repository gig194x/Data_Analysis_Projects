/*_______________________ SQL Server  SSMS__________________________*/

-- Count number of books per author  
SELECT 
    a.author_name,
    COUNT(b.title) AS BooksCount
FROM books_clean_with_authors_ids_sales b
JOIN authors_names_w_ids a 
    ON b.author_id = a.author_id
GROUP BY a.author_name
ORDER BY BooksCount DESC;



-- Top 5 Authors by Revenue  
SELECT TOP 5
    a.author_name,
    CAST(SUM(b.price * b.sales_units) AS DECIMAL(10,2)) AS total_revenue
FROM books_clean_with_authors_ids_sales b
JOIN authors_names_w_ids a 
    ON b.author_id = a.author_id
GROUP BY a.author_name
ORDER BY total_revenue DESC;



-- Bottom 5 Authors by Revenue 
SELECT TOP 5
    a.author_name,
    CAST(SUM(b.price * b.sales_units) AS DECIMAL(10,2)) AS total_revenue
FROM books_clean_with_authors_ids_sales b
JOIN authors_names_w_ids a 
    ON b.author_id = a.author_id
GROUP BY a.author_name
ORDER BY total_revenue ASC;




-- Top 5 Best-Selling Books 

SELECT TOP 5
    b.title,
    SUM(b.price * b.sales_units) AS total_revenue
FROM books_clean_with_authors_ids_sales b
GROUP BY b.title
ORDER BY total_revenue DESC;



--Bottom 5 Lowest-Selling Books  
SELECT TOP 5
    b.title,
    SUM(b.price * b.sales_units) AS total_revenue
FROM books_clean_with_authors_ids_sales b
GROUP BY b.title
ORDER BY total_revenue ASC;



-- Compare book ratings with sales performance 
SELECT 
    b.title,
    b.rating,
    SUM(b.sales_units) AS total_units_sold
FROM books_clean_with_authors_ids_sales b
GROUP BY b.title, b.rating
ORDER BY b.rating DESC, total_units_sold DESC;

-------------------------------------------------------------------------------


/*_______________________ BigQuery __________________________*/

/* Top 1 selling book */

--Top 1 selling book
SELECT
    b.title,
    b.rating,
    b.sales_units,
    b.price
FROM `silver-archery-472213-n5.Online_bookstore.Online_store` b
ORDER BY b.sales_units DESC
LIMIT 1;



--Calculate averages grouped by Rating
SELECT
    b.rating,
    AVG(b.sales_units) AS Avg_Sales,
    AVG(b.price) AS Avg_Price
FROM `silver-archery-472213-n5.Online_bookstore.Online_store` b
GROUP BY b.rating
ORDER BY b.rating DESC;
