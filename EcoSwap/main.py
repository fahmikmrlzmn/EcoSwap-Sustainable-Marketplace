from database import create_tables
from marketplace import add_item, view_items, search_by_category, send_message

def menu():
    print("\n🌱 EcoSwap – Sustainable Marketplace")
    print("1. Add item for sale")
    print("2. View all items")
    print("3. Search items by category")
    print("4. Send message to seller")
    print("5. Exit")

def main():
    create_tables()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            send_message()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
