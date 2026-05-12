SELECT DISTINCT name AS unique_supplier
FROM suppliers
ORDER BY name;

SELECT 
    name AS supplier_name,
    COUNT(*) AS products_supplied,
    COUNT(DISTINCT product_id) AS distinct_products
FROM suppliers
GROUP BY name
ORDER BY name;