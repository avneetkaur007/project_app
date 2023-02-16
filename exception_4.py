class BalanceException(Exception):
    pass
def chkbalance():
    money=10000
    withdraw=7000
    try:
        bal=money-withdraw
        if(bal<=2000):
            raise BalanceException('insufficient balance')
        print(bal)
    except BalanceException as b:
        print(b)
chkbalance()