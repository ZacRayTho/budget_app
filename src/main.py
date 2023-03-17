import random
from category import Category

class Budget():
    def __init__(self, attr):
        for x in range(len(attr)):
            setattr(self, attr[x], Category(attr[x]))

    def split_deposit(self, amount, desc = "paycheck"):
        x = amount / len(vars(self))
        self.food.deposit(x, desc)
        self.clothes.deposit(x, desc)
        self.auto.deposit(x, desc)
        self.hobby.deposit(x, desc)
        self.bills.deposit(x, desc)

    
list = ["food", "clothes", "auto", "hobby", "bills"]

my_wallet = Budget(list)

my_wallet.split_deposit(random.randint(100, 5000))

for x in list:
    exec(f"my_wallet.{x}.transfer(random.randint(0, int(my_wallet.{x}.funds)), my_wallet.{list[random.randint(0, len(list) - 1)]})")
    exec(f"my_wallet.{x}.withdraw(random.randint(0, int(my_wallet.{x}.funds)), 'mafia protection')")
    exec(f"my_wallet.{x}.deposit(random.randint(1, 5000), 'doordash')")
    
for x in list:
    exec(f"print(my_wallet.{x})")
    
