-- Write your query below
SELECT name 
FROM sales_person
WHERE sales_id NOT IN (
    SELECT orders.sales_id
    FROM orders, company
    WHERE company.name = 'CRIMSON' AND orders.com_id = company.com_id
)