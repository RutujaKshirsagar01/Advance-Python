class Product:
    def __init__(self, pid, name, quantity, price):
        self.pid = pid
        self.name = name
        self.quantity = quantity
        self.price = price

    def display(self):
        print(f"ID: {self.pid},  Name: {self.name},   Quantity: {self.quantity},   Price: {self.price}")

products = {}

while True:
    print("""\n === Product Inventory System ===
          1. Add Product
          2. List Products
          3. Update Product
          4. Search Product
          5. Remove Product
          6.Exit""")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = int(input("Enter Product ID: "))
        if pid in products:
            print("Product ID already exists.")
        else:
            name = input("Enter Product Name: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))

            products[pid] = Product(pid, name, quantity, price)
            print("Product added successfully.")

    elif choice == 2:
        if not products:
            print("No products available.")
        else:
            print("\n--- Product List ---")
            for p in products.values():
                p.display()

    elif choice == 3:
        pid = int(input("Enter Product ID to update: "))
        if pid in products:
            print("""\n === Product Update ===
                  1. Name
                  2. Quantity
                  3. Price""")
            ch=int(input("Enter your choice(1-3): "))
            if ch == 1:
                name = input("Enter new name: ")
                products[pid].name = name
                print("Name update successfully.")
            elif ch == 2:
                quantity = int(input("Enter new quantity: "))
                products[pid].quantity = quantity
                print("Product Quantity update successfully.")
            elif ch == 3:
                price = float(input("Enter new price: "))
                products[pid].price = price
                print("Product Price updated successfully.")
            
            else:
                print("Enter valid Choice.")            
        else:
            print("Product not found.")

    elif choice == 4:
        pid = int(input("Enter Product ID to search: "))
        if pid in products:
            print("\n--- Product Found ---")
            products[pid].display()
        else:
            print("Product not found.")

    elif choice == 5:
        pid = int(input("Enter Product ID to remove: "))
        if pid in products:
            del products[pid]
            print("Product removed successfully.")
        else:
            print("Product not found.")

    elif choice == 6:
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Please select between 1 and 6.")
