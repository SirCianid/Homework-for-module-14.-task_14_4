import sqlite3


def initiate_db(db_path='Products_db.db'):
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')
    connect.commit()
    connect.close()


def add_product(title, description, price, db_path='Products_db.db'):
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   (title, description, price))
    connect.commit()
    connect.close()


def get_all_products(db_path='Products_db.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    conn.close()
    return products


initiate_db()

add_product(title='Аскорбиновая кислота', description='Классические аскорбинки, в формате желтых шариков', price=100)
add_product(title='Компливит для детей', description='Мультивитаминный комплекс для детей в формате желейных конфет',
            price=200)
add_product(title='Herbal Vitamins',
            description='Травяной витаминный комплекс в капсулах, на основе лекарственных растений', price=300)
add_product(title='Рыбий жир', description='Очищеный рыбий жир в капсулах, источник омега-3', price=400)
