from category import Category

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

# You can write tests here or create new files in this directory with the name test_[something].py