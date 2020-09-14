accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}


def add_balance(amount: float, name: str ='checking') -> float:
    """
    Function to update the balance of an account and return the new balance.
    """
    accounts[name] += amount
    return accounts[name]


transctions = [
    (-180.67, "checking"),
    (-220.00, 'checking'),
    (220.00, 'savings'),
    (-15.70, 'checking'),
    (-23.90, 'checking'),
    (-13.00, 'checking'),
    (1579.50, 'checking'),
    (-600.50, 'checking'),
    (600.500, 'savings')
]

for t in transctions:
    add_balance(*t)