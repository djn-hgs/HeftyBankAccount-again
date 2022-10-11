import pytest
import main


@pytest.fixture
def the_bank():
    return main.Bank()


@pytest.fixture
def alice():
    return main.Person('Alice', 'Tree')


@pytest.fixture
def bob():
    return main.Person('Bob', 'Sapling')


@pytest.fixture
def alice_account(the_bank, alice):
    return main.BankAccount(1, the_bank, alice, 0)


@pytest.fixture
def bob_account(the_bank, bob):
    return main.BankAccount(1, the_bank, bob, 0)


def test_credit(alice_account):
    alice_account.credit_balance(200)
    assert alice_account.balance == 200


def test_debit(alice_account):
    alice_account.credit_balance(200)
    alice_account.debit_balance(200)
    assert alice_account.balance == 0
