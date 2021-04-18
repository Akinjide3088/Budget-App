class Categories:

    def __init__(self, name, ledger):
        self.name = name
        self.ledger = []    


    def deposit(self, amount, description):

        self.ledger.append({"amount": amount, "description": description})
        

    def withdrawal(self, amount, description ):

        if(self.check_funds(amount)):
            
            self.ledger.append({"amount":-amount, "description": description})
            return True
        return False

      
    def compute_bal(self):
        
        total_cash = 0

        for item in self.ledger:
            total_cash += item["amount"]

        return total_cash


    def transfer_bal(self, amount, category):

        if(self.check_funds(amount)):

            self.withdraw(amount, "Transfer to" + category.item)
            category.deposit(amount, "Transfer from" + self.name)
            return True
        return False

    def check_funds(self, amount):
        
        if (self.compute_balance() >= amount):
            return True
        return False



food = Category("food")
food.deposit(1000, "initial deposit")
food.withdraw(10.5, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25,55)
print(clothing.get_balance())

entertainment = Category("Entertainment")
entertainment.deposit(1000, "intial deposit")
entertainment.withdraw(15)
print(entertainment.get_balance())

print(food)
print(clothing)
print(entertainment)









