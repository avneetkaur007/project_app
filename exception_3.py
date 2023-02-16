#user defined exceptions
class BalanceException(Exception):
    pass
def chkbalance():
    money=10000
    withdraw=5000
    bal=money-withdraw
    print(bal)
chkbalance()