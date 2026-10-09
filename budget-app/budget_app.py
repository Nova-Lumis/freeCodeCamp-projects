'''
Simple Budget App
Aim:
- Tracking spending money on different categories
- Relative spending percentage on a graph.
'''

# Category 
class Category:
    # Instance attributes
    def __init__(self, name: str) -> None:
        self.name = name
        # Ledger contains list of transactions
        self.ledger = []
    

    # deposit method add an amount in a single transaction
    def deposit(self, amount: float, description = "") -> None:
        self.ledger.append({
            "amount": amount,
            "description": description
        })
        # print("Deposit success.")
    
    # withdraw method
    def withdraw(self, amount: float, description = "") -> bool:
        if not self.check_funds(amount):
            # print("Withdraw Failed")
            return False
        
        # add withdraw transaction to ledger 
        self.ledger.append({
            "amount": -amount,
            "description": description
        })
        # print("Withdraw Success")
        return True
       
    
    # return the balance of a certain category
    def get_balance(self) -> float:
        balance = 0
        for ledger in self.ledger:
            for key, value in ledger.items():
                if key == "amount":
                    balance += value
        return balance
    
    # transfer
    def transfer(self, amount: float, other_category) -> bool:
        # withdraw and transfer the amount to another category
        transferred = self.withdraw(amount, f"Transfer to {other_category.name}")
        
        # the category the amount transferred to, should accept the amount as deposit.
        if transferred:
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        
        return False
    
    # Check if the balance higher than the withdrawal amount
    def check_funds(self, amount) -> bool:
        return self.get_balance() >= amount 
    
    # return a string when category is called
    def __str__(self):
        display = ""
        display += self.name.center(30, "*") + "\n"

        for i in self.ledger:
            display += i['description'][:23].ljust(23) + f"{i['amount']:.2f}".rjust(7) + "\n"
        
        display += (f"Total: {self.get_balance()}")

        return display


# Views the percentage withdrawal by the category
def create_spend_chart(categories) -> str:
    categories_withdrawal = []
    categories_name = []

    total_withdrawal = 0
    for category in categories:
        withdrawal_amount = 0
        # Append the name of category
        categories_name.append(category.name)

        for j in category.ledger:
            amount = j["amount"]
            if amount < 0:
                withdrawal_amount += amount
                total_withdrawal += amount
        withdrawal_amount *= -1
        categories_withdrawal.append(withdrawal_amount)
    
    # positive total withdraw
    total_withdrawal *= -1

    # Updating the categories withdraw into total percentage spent.
    for i, withdraw in enumerate(categories_withdrawal):
        # calculating the percentage
        withdraw = (withdraw / total_withdrawal) * 100 
        # rounded down to nearest 10
        withdraw = (withdraw // 10) * 10
        # changing the value on the original list
        categories_withdrawal[i] = withdraw
    
    # # display list
    # print(categories_name)
    # print(categories_withdrawal)

    # displaying the chart
    full_line = ""
    full_line += "Percentage spent by category\n"
    for i in range(100, -10, -10):
        line = ""
        # Adding the number
        line += str(i).rjust(3) + "| "
        
        # Adding the " o "
        for percent_category in categories_withdrawal:
            if percent_category >= i:
                line += "o  "
            else:
                line += "   " 
        full_line += line + "\n"

    # Adding the horizontal line
    full_line += "    " + "-" * (len(categories) * 3) + "-\n"

    # Adding the horizontal name
    max_label_len = max(len(name) for name in categories_name)
    
    # Looping for each string on each category name
    for i in range(max_label_len):
        line = "     "
        for j in categories_name:
            if i < len(j):
                line += j[i] + "  "
            else:
                line += "   "
        if i < max_label_len - 1:
            line += "\n"
        full_line += line

    return full_line


# # Main trial
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

# displaying the list
print(food)
print("\n")
print(clothing)
print("\n")

# displaying chart
print(create_spend_chart([food, clothing]))




