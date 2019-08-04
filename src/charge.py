class Charge(object):
    """ Payment per hour basis """

    def __init__(self, two_wheeler_price, four_wheeler_price):
        self._two_wheeler_price = two_wheeler_price
        self._four_wheeler_price = four_wheeler_price

    @property
    def two_wheeler_price(self):
        return self._two_wheeler_price

    @property
    def four_wheeler_price(self):
        return self._four_wheeler_price

    @two_wheeler_price.setter
    def two_wheeler_price(self, two_wheeler_price):
        self._two_wheeler_price = two_wheeler_price

    @four_wheeler_price.setter
    def four_wheeler_price(self, four_wheeler_price):
        self._four_wheeler_price = four_wheeler_price


# c = Charge(100, 200)

# print(c)

# print(c.four_wheeler_price)

# print(vars(c))

# c.four_wheeler_price = 330

# print(c.four_wheeler_price)
