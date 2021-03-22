import pytest
from .Account import Account

@pytest.fixture(autouse=True)
def run_around_tests():
    yield
    # We need to reset the Account class variables between tests.
    Account.reset()

def test_first_account_gets_number_1():
    account = Account()
    assert account.number == 1

@pytest.fixture
def two_accounts():
    Account()
    Account()

def test_number_of_accounts_increases_on_creation(two_accounts):
    assert Account.numberOfAccounts == 2

# Write your tests below here.

def test_initial_amount_is_set_on_account_creation():
    initial_amount = 300.0
    account = Account(initial_amount)
    assert account.balance == initial_amount