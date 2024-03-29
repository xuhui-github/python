from decimal import Decimal


class Fees(object):

    def __init__(self):
        self._fee = None

    def get_fee(self):
        return self._fee

    def set_fee(self, value):
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value


if __name__ == "__main__":
    f = Fees()
    f.set_fee("1")
    print(f.get_fee())
