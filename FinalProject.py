# Define the inventory list
inventory = []


# Function to add an item to the inventory
def add_item(name, price, quantity, category):
    item = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'category': category
    }
    inventory.append(item)


# Function to update an item in the inventory
def update_item(name, price=None, quantity=None, category=None):
    for item in inventory:
        if item['name'] == name:
            if price is not None:
                item['price'] = price
            if quantity is not None:
                item['quantity'] = quantity
            if category is not None:
                item['category'] = category
            return f"{name} updated successfully."
    return f"{name} not found in inventory."


# Function to view the inventory
def view_inventory():
    if not inventory:
        print("The inventory is empty.")
    else:
        for item in inventory:
            print(
                f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}, Category: {item['category']}")


# Function to remove an item from the inventory
def remove_item(name):
    for item in inventory:
        if item['name'] == name:
            inventory.remove(item)
            return f"{name} removed successfully."
    return f"{name} not found in inventory."


# Function to search for items by category
def search_by_category(category):
    found_items = [item for item in inventory if item['category'] == category]
    if not found_items:
        print(f"No items found in category: {category}")
    else:
        for item in found_items:
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")


# Main loop to interact with the user
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            category = input("Enter item category: ")
            add_item(name, price, quantity, category)
            print(f"{name} added to the inventory.")
        elif choice == '2':
            name = input("Enter the name of the item to update: ")
            price = input("Enter new price (or press Enter to skip): ")
            quantity = input("Enter new quantity (or press Enter to skip): ")
            category = input("Enter new category (or press Enter to skip): ")
            update_result = update_item(name, float(price) if price else None, int(quantity) if quantity else None,
                                        category if category else None)
            print(update_result)
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            name = input("Enter the name of the item to remove: ")
            remove_result = remove_item(name)
            print(remove_result)
        elif choice == '5':
            category = input("Enter category to search: ")
            search_by_category(category)
        elif choice == '6':
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
