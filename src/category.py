class Category():
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.funds = 0

    def deposit(self, amount, description = " "):
        self.funds += amount
        self.ledger.append({"amount": amount, "description": description})
        

    def withdraw(self, amount, description = " "):
        if self.check_funds(amount):
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

    def check_funds(self, amount):
        if self.funds >= amount:
            return False
        else:
            return True

    def __str__(self):
        print(f"""**************{self.name}**************""")
        for x in self.ledger:
            print(f"{x['description']:<10} {x['amount']:>20}")
        return f"Total: {self.funds}" 

