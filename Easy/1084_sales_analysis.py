"""
1084. Sales Analysis III

Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
| unit_price   | int     |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the name and the price of each product.
Table: Sales

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| seller_id   | int     |
| product_id  | int     |
| buyer_id    | int     |
| sale_date   | date    |
| quantity    | int     |
| price       | int     |
+-------------+---------+
This table can have duplicate rows.
product_id is a foreign key (reference column) to the Product table.
Each row of this table contains some information about one sale.

Write a solution to report the products that were only sold in the first quarter of 2019.
That is, between 2019-01-01 and 2019-03-31 inclusive.

Return the result table in any order.
"""

sql_query = """
SELECT temp.product_id, Product.product_name
    (SELECT product_id
    FROM Sales
    GROUP BY product_id
    HAVING 
        min(sale_date) >= '2019-01-01'
        AND
        max(sale_date) <= '2019-03-31'
    ) AS temp
LEFT JOIN Product ON temp.product_id = Product.product_id
"""

sql_query = """
SELECT Sales.product_id, Product.product_name
FROM Sales
LEFT JOIN Product
ON Product.product_id=Sales.product_id
GROUP BY Sales.product_id
HAVING MIN(sale_date) >= CAST('2019-01-01' AS DATE)
    AND
       MAX(sale_date) <= CAST('2019-03-31' AS DATE)
"""

sql_query = """
SELECT product_id, product_name
FROM Products
WHERE product_id IN
    (SELECT product_id
     FROM Sales
     GROUP BY product_id
     HAVING MIN(sale_date) >= CAST('2019-01-01' AS DATE)
        AND
            MAX(sale_date) <= CAST('2019-03-31' AS DATE)
    )
"""