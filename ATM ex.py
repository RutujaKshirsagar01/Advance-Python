class ATM:
    def __init__(self, acc_no, name, bal):
        self.acc_no = acc_no
        self.name = name
        self.bal = bal

    def deposit(self, amount):
        if amount > 0:
            self.bal =self.bal + amount
            print("Deposited Amount:", amount)
        else:
            print("Invalid deposit amount.")
        print("Current Balance:", self.bal)

    def withdraw(self, wamount):
        if wamount > 0 and wamount <= self.bal:
            self.bal -= wamount
            print("Withdrawn Amount:", wamount)
        else:
            print("Invalid or insufficient funds.")
        print("Current Balance:", self.bal)

    def display(self):
        print(f"Account Number: {self.acc_no}, Name: {self.name}, Balance: {self.bal}")

users = {123: ATM(123, "Aryan", 30000),456: ATM(456, "Neha", 50000),789: ATM(789, "Rahul", 15000)}

while True:
    print("\n==== ATM System ====")
    print("1. Select Account")
    print("2. Create New Account")
    print("3. Exit")

    main_choice = int(input("Enter your choice: "))

    if main_choice == 1:
        acc = int(input("Enter your account number: "))
        if acc in users:
            user = users[acc]
            while True:
                print(f"\n--- Welcome {user.name} ---")
                print("1. Display")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Logout")

                ch = int(input("Enter your choice: "))
                if ch == 1:
                    user.display()
                elif ch == 2:
                    amt = int(input("Enter amount to deposit: "))
                    user.deposit(amt)
                elif ch == 3:
                    amt = int(input("Enter amount to withdraw: "))
                    user.withdraw(amt)
                elif ch == 4:
                    print("Logging out...\n")
                    break
                else:
                    print("Invalid option.")

        else:
            print("Account not found.")

    elif main_choice == 2:
        acc_no = int(input("Enter new account number: "))
        if acc_no in users:
            print("Account already exists.")
        else:
            name = input("Enter account holder name: ")
            bal = int(input("Enter initial balance: ₹"))
            users[acc_no] = ATM(acc_no, name, bal)
            print("Account created successfully.")

    elif main_choice == 3:
        print("Exiting ATM system.")
        break
    else:
        print("Invalid main menu choice.")
