from database import connect_db

def add_item():
    name = input("Item name: ")
    category = input("Category: ")
    price = float(input("Price (RM): "))
    condition = input("Condition: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO items (name, category, price, condition) VALUES (?, ?, ?, ?)",
        (name, category, price, condition)
    )

    conn.commit()
    conn.close()
    print("✅ Item added successfully!")

def view_items():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()

    if not items:
        print("No items available.")
    else:
        for item in items:
            print(item)

    conn.close()

def search_by_category():
    category = input("Enter category to search: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items WHERE category = ?", (category,))
    items = cursor.fetchall()

    if not items:
        print("No items found in this category.")
    else:
        for item in items:
            print(item)

    conn.close()

def send_message():
    item_id = int(input("Enter item ID: "))
    message = input("Enter your message: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages (item_id, message) VALUES (?, ?)",
        (item_id, message)
    )

    conn.commit()
    conn.close()
    print("💬 Message sent!")
