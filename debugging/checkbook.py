class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Please enter a positive amount to deposit.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a positive amount to withdraw.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        
        if action == 'exit':
            print("Goodbye!")
            break
        
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                continue
            cb.deposit(amount)
        
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                continue
            cb.withdraw(amount)
        
        elif action == 'balance':
            cb.get_balance()
        
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()