import psycopg2

connection = None
cursor = None

try:

    connection = psycopg2.connect(
        host="localhost",
        port="5433",
        user="postgres",
        password="example",
        database="testdb"
    )
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name, category 
        FROM products 
        LIMIT 10;
    """)

    rows = cursor.fetchall()

    print("Список товаров:")
    print("-" * 40)
    for row in rows:
        print(f"Товар: {row[0]}, Категория: {row[1]}")

    print("-" * 40)
    print(f"Всего выведено товаров: {len(rows)}")

    cursor.close()
    connection.close()

except Exception as error:
    print(f"Ошибка при подключении или выполнении запроса: {error}")
    if connection:
        connection.rollback()
    if cursor:
        cursor.close()
    if connection:
        connection.close()