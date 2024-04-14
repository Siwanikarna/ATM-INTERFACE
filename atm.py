from tabulate import tabulate
import sys

class ATM:
    def __init__(self):
        self.initial_balance = 100000
        self.balance = self.initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            return 'Invalid amount. Please enter a positive value.'
        self.balance += amount
        transaction_detail = f'Deposited ${amount}'
        self.transaction_history.append(transaction_detail)
        return f'\nDeposited ${amount}\nNew balance: ${self.balance}'

    def withdraw(self, amount):
        if amount <= 0:
            return 'Invalid amount. Please enter a positive value.'
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        self.transaction_history.append(f'Withdrawn ${amount}')
        return f'\nWithdrawn ${amount}\nNew balance: ${self.balance}'

    def transfer(self, amount, recipient, transfer_type):
        if amount <= 0:
            return 'Invalid amount. Please enter a positive value.'
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        transaction_detail = f'Transferred ${amount} to {recipient}'
        self.transaction_history.append(transaction_detail)
        return f'Transferred ${amount} to {recipient}\nNew balance: ${self.balance}'

    def get_balance(self):
        return f'Current balance: ${self.balance}'

    def get_transaction_history(self):
        return self.transaction_history


def atm_interface():
    atm = ATM()

    print("\n*****Welcome to the ATM Interface by Siwani Karna*****")

    user_id = input("\nEnter User ID: ")
    pin = input("Enter PIN: ")

    if user_id == "123456" and pin == "654321":
        print("\nLogin successful!")

        while True:
            print("\nATM Operations:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Quit\n")

            choice = input("\nEnter your choice (1/2/3/4/5/6): ")

            if choice == "1":
                try:
                    amount = float(input("\nEnter the deposit amount: $"))
                    result = atm.deposit(amount)
                    print(f"{result}")
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            elif choice == "2":
                try:
                    amount = float(input("\nEnter the withdrawal amount: $"))
                    result = atm.withdraw(amount)
                    print(f"{result}")
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            elif choice == "3":
                try:
                    amount = float(input("Enter the transfer amount: $"))
                    recipient = input("\nEnter the recipient's name: ")
                    transfer_details = f"\nRecipient: {recipient}"
                    result = atm.transfer(amount, transfer_details, 3)
                    print(f'{result}')
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            elif choice == "4":
                balance = atm.get_balance()
                print(f"\n{balance}")
            elif choice == "5":
                history = atm.get_transaction_history()
                if len(history) > 0:
                    table = []
                    for i, transaction in enumerate(history, start=1):
                        table.append([i, transaction])
                    print(tabulate(table, headers=["#", "Transaction"], tablefmt="grid"))
                else:
                    print("\nTransaction history is empty.")
            elif choice == "6":
                print("\nThank you for using ATM. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter a valid option.")

        continue_choice = input("\nDo you want to perform another transaction? (yes/no): ")

        if continue_choice.lower() != "yes":
            print("\nThank you for using ATM. Goodbye!")
    else:
        print("\nInvalid User ID or PIN. Exiting...")
        sys.exit() 

if __name__ == "__main__":
    atm_interface()
