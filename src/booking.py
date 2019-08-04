from capacity import Capacity
from vehicle import Vehicle
from charge import Charge


class Payment(object):
    def __init__(self, two_wheeler_price, four_wheeler_price, time):
        self.charge = Charge(two_wheeler_price, four_wheeler_price)
        self.time = time

    def amount(self):
        return self.charge.two_wheeler_price * self.time


p = Payment(12, 25, 5)
print(p.amount())

print(vars(p))


capacity = Capacity(10, 13)


class Booking(object):

    _count = capacity

    def __init__(self, v_type, reg_number):
        self._vechile = Vehicle(v_type, reg_number)

    def __new__(cls, v_type, req_number):
        if v_type == 'two_wheeler':
            if cls._count._two_wheeler < 1:
                print("No space available  for two wheeler sorry !!!!")
            else:
                cls._count._two_wheeler -= 1
                return object().__new__(cls)
        if v_type == 'four_wheeler':
            if cls._count._four_wheeler < 1:
                print("ooops no space for Cars ")
            else:
                cls._count._four_wheeler -= 1
                return object().__new__(cls)
        else:
            return object().__new__(cls)


print(vars(Booking))

# print(Booking._count._two_wheeler)
b = Booking('two_wheeler', 123)


print(Booking._count._two_wheeler)

print(b._vechile.v_type)

c = Booking('two_wheeler', 124)

print(c)

print(Booking._count._two_wheeler)

# c = Capacity(10, 12)
# print(c.capacity_two_wheeler)
# print(c.capacity_four_wheeler)

# c.capacity_two_wheeler = 1

# print(c.capacity_two_wheeler)


# v = Vehicle('two_wheeler', 123456)

# print(vars(v))

# print(v.v_type)
