class InvalidWithdraw1(Exception):
    def __init__(self,balance,amount):
        super().__init__("account does't have ${}".format(amount))
        self.balance=balance
        self.amount=amount

    def overage(self):
        return self.amount-self.balance

#raise InvalidWithdraw1(25,50)

if __name__ == '__main__':
    try:
        raise InvalidWithdraw1(25,50)
    except InvalidWithdraw1 as e:
        print("I'm sorry,but your withdrawa1 is "
              "more than your balance by "
              "${}".format(e.overage()))

