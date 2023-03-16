from category import Category
from pytest import *
# category has class type
def test_category_class():
    c = Category("bob")
    assert isinstance(c, Category)

# has name attribute
def test_category_name():
    c = Category("bob")
    assert hasattr(c, "name")

# has instance variable of "ledger"
def test_category_ledger():
    c = Category("bob")
    assert hasattr(c, "ledger")

# "ledger" variable is a list
def test_category_ledger_type():
    c = Category("bob")
    assert isinstance(c.ledger, list)

# has deposit method
def test_category_deposit():
    c = Category("bob")
    assert callable(c.deposit)

# has withdraw method
def test_category_withdraw():
    c = Category("bob")
    assert callable(c.withdraw)

# has get_balance method
def test_category_get_balance():
    c = Category("bob")
    assert callable(c.get_balance)

# has transfer method
def test_category_transfer():
    c = Category("bob")
    assert callable(c.transfer)

# has check_funds method
def test_category_check_funds():
    c = Category("bob")
    assert callable(c.check_funds)

# deposit method accepts an amount and description 
def test_category_deposit_amount_description():
    c = Category("bob")

    # raises is a pytest function
    # it passes if an Exception was thrown because of an error 
    # in this test ,the exception I'm expecting is TypeError because there was
    #   no parameters passed to the function
    # so it passed because it threw the error i was expecting
    # If I put ValueError , it would fail because the function didn't fail 
    #   because of a ValueError
    with raises(TypeError):
        c.deposit()

# if deposit doesn't get a description , it defaults to empty
def test_category_deposit_description_defaults():
    c = Category("bob")
    c.deposit(10)
    assert c.ledger[0]["description"] == " "

# deposit method appends object to ledger list
def test_category_ledger_deposit_append():
    c = Category("bob")
    c.deposit(10, "fish")
    assert c.ledger[0] == {"amount": 10, "description": "fish"}

# withdraw method accepts an amount and description 
def test_category_withdraw_amount_description():
    c = Category("bob")

    with raises(TypeError):
        c.withdraw()

# if withdraw doesn't get a description , it defaults to empty
def test_category_withdraw_description_defaults():
    c = Category("bob")
    c.deposit(10, "fish")
    c.withdraw(10)
    assert c.ledger[1]["description"] == " "

# withdraw method appends object to ledger list
def test_category_ledger_withdraw_append():
    c = Category("bob")
    c.deposit(10, "fish")
    c.withdraw(10, "fish")
    assert c.ledger[1] == {"amount": -10, "description": "fish"}

# withdraw method stores negative number
def test_category_ledger_withdraw_negative_value():
    c = Category("bob")
    c.deposit(10, "fish")
    c.withdraw(10, "fish")
    assert c.ledger[1]["amount"] < 0

# if withdraw method is more than fund, don't add to ledger
def test_category_withdraw_over_funds():
    c = Category("bob")
    c.withdraw(10, "fish")
    assert c.ledger == []

# deposit method should increase fund variable
def test_category_deposit_funds_increase():
    c = Category("bob")
    c.deposit(10, "fish")
    assert c.funds > 0

# withdraw method returns True if append to ledger happened, else False
def test_category_withdraw_return_false():
    c = Category("bob")
    assert c.withdraw(10, "fish") == False
    
def test_category_withdraw_return_true():
    c = Category("bob")
    c.deposit(20)
    assert c.withdraw(10, "fish") == True

# get balance method returns current balance of category
def test_category_get_balance_return():
    c = Category("bob")
    c.deposit(50, "fish")
    c.withdraw(20)
    c.deposit(75)
    c.withdraw(50)
    assert c.get_balance() == 55

# You can write tests here or create new files in this directory with the name test_[something].py