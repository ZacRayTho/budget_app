class Category():
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.funds = 0

    def deposit(self, amount, description = " "):
        self.funds += amount
        self.ledger.append({"amount": amount, "description": description})
        

    def withdraw(self, amount, description = " "):
        if amount > self.funds:
            return False
        else:
            self.funds -= amount
            self.ledger.append({"amount": 0 - amount, "description": description})
            return True

    def get_balance(self):
        return self.funds

    def transfer(self, amount, target_category):
        if self.withdraw(amount, f"Transfer to {target_category.name}") == True:
            target_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else: 
            return False
            
    def check_funds(self):
        pass

