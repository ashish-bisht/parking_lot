class Capacity(object):
    """ setting capacity of various  """

    def __init__(self, two_wheeler, four_wheeler):
        self._two_wheeler = two_wheeler
        self._four_wheeler = four_wheeler

    @property
    def capacity_two_wheeler(self):
        return self._two_wheeler

    @property
    def capacity_four_wheeler(self):
        return self._four_wheeler

    @capacity_two_wheeler.setter
    def capacity_two_wheeler(self, two_wheeler):
        self._two_wheeler = two_wheeler

    @capacity_four_wheeler.setter
    def capacity_four_wheeler(self, four_wheeler):
        self._four_wheeler = four_wheeler


# c = Capacity(150, 25)

# print(c.capacity_two_wheeler)
# print(c.capacity_four_wheeler)

# c.capacity_two_wheeler = 1

# print(c.capacity_two_wheeler)
