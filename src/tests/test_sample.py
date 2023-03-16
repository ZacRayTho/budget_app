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

# You can write tests here or create new files in this directory with the name test_[something].py