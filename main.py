class Person:
    def __init__(self, forename, surname):
        self.forename = forename
        self.surname = surname


class Bank:
    def __init__(self):
        self.account_roster = []
        self.activity_log = ''

    def log_event(self, log_string):
        self.activity_log += '\n' + log_string

    def add_account(self, account: BankAccount):
        self.account_roster.append(account)
        self.log_event(f'Added account {account.get_code()}.')

    def close_account(self, account: BankAccount):
        if account not in self.account_roster:
            raise Exception(f'Account {account.get_code()}.')
        if account.get_balance() != 0:
            raise Exception(f'Trying to close account {account.get_code()}: account needs to be empty.')

        del(self.account_roster, account)
        self.log_event(f'Account {account.get_code()} closed.')

    def transfer_money(self, source: BankAccount, destination: BankAccount, amount: float):
        source.debit_balance(amount)
        destination.credit_balance(amount)
        self.log_event(f'Transfer of {amount} from {source.get_code()} to {destination.get_code()} complete.')


class BankAccount:
    def __init__(self, account_code: int, bank: Bank, owner: Person, opening_balance: float = 0):
        self.owner = owner
        self.balance = opening_balance
        self.account_code = account_code
        self.bank = bank

    def get_code(self):
        return self.account_code

    def credit_balance(self, credit):
        if credit < 0:
            raise ValueError('Must be a positive credit')
        self.balance += credit
        self.bank.log_event(f'Credited {credit} to account {self.account_code}. Balance is now {self.balance}.')

    def debit_balance(self, debit):
        if debit < 0:
            raise ValueError('Must be a positive debit')
        self.balance -= debit
        self.bank.log_event(f'Credited {debit} to account {self.account_code}. Balance is now {self.balance}.')

    def get_balance(self):
        self.bank.log_event(f'Balance enquiry. Balance is now {self.balance}.')
        return self.balance


