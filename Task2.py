#NamedTuple and defaultdict

from collections import defaultdict

account_balances = defaultdict(lambda:15)

deposits = {'Jonathan' : 0.49,
            'Markus':0.39,
            'Jamshed': 100}

for account,deposit in deposits.items():
    account_balances[account] += deposit

print(dict(account_balances))

from collections import defaultdict
from typing import NamedTuple
class Deposit(NamedTuple):
    receiver:str
    value:float

account_balances = defaultdict(lambda:15)

deposits = [Deposit(receiver='Jonathan', value=0.49),
            Deposit(receiver='Markus', value=0.39),
            Deposit(receiver='Jamsheed', value=100)]

for deposit in deposits:
    account_balances[deposit.receiver] += deposit.value

print(dict(account_balances))
