\echo '=== ЗАДАНИЕ 1: ТОВАРЫ ==='
SELECT '1. Все товары (первые 5 из 62)' AS query;
SELECT * FROM products LIMIT 5;

SELECT '2. Название и категория (первые 5)' AS query;
SELECT name, category FROM products LIMIT 5;

SELECT '3. Уникальные категории' AS query;
SELECT DISTINCT category FROM products;

SELECT '4. Сортировка по названию (А-Я) - первые 5' AS query;
SELECT * FROM products ORDER BY name ASC LIMIT 5;

SELECT '5. Сортировка по названию (Я-А) - первые 5' AS query;
SELECT * FROM products ORDER BY name DESC LIMIT 5;

SELECT '6. Первые 10 товаров' AS query;
SELECT * FROM products LIMIT 10;

SELECT '7. Товары с 11-й позиции (10 шт.)' AS query;
SELECT * FROM products LIMIT 10 OFFSET 10;

SELECT '8. 5 случайных товаров' AS query;
SELECT * FROM products ORDER BY RANDOM() LIMIT 5;

SELECT '9. Все категории (с повторами) - первые 10' AS query;
SELECT category FROM products ORDER BY category ASC LIMIT 10;

SELECT '10. Сортировка: категория -> название (первые 10)' AS query;
SELECT * FROM products ORDER BY category ASC, name ASC LIMIT 10;

\echo '=== ЗАДАНИЕ 2: ЦЕНЫ ==='

SELECT '1. 5 самых дорогих товаров' AS query;
SELECT p.name, pr.price, pr.created_at
FROM prices pr
JOIN products p ON pr.product_id = p.product_id
ORDER BY pr.price DESC
LIMIT 5;

SELECT '2. 10 последних добавленных цен' AS query;
SELECT p.name, pr.price, pr.created_at
FROM prices pr
JOIN products p ON pr.product_id = p.product_id
ORDER BY pr.created_at DESC
LIMIT 10;

SELECT '3. 10 самых дешёвых цен' AS query;
SELECT p.name, pr.price, pr.created_at
FROM prices pr
JOIN products p ON pr.product_id = p.product_id
ORDER BY pr.price ASC
LIMIT 10;

SELECT '4. Цены: пропустить 20 самых дорогих, показать следующие 10' AS query;
SELECT p.name, pr.price, pr.created_at
FROM prices pr
JOIN products p ON pr.product_id = p.product_id
ORDER BY pr.price DESC
LIMIT 10 OFFSET 20;

\echo '=== ЗАДАНИЕ 3: ПОСТАВЩИКИ ==='

SELECT '1. Список уникальных поставщиков' AS query;
SELECT DISTINCT name AS supplier_name
FROM suppliers
ORDER BY name;

SELECT 'Дополнительно: количество товаров от каждого поставщика' AS query;
SELECT 
    name AS supplier_name,
    COUNT(*) AS total_supplies,
    COUNT(DISTINCT product_id) AS unique_products
FROM suppliers
GROUP BY name
ORDER BY total_supplies DESC
LIMIT 10;