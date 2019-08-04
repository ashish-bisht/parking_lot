class Vehicle(object):
    """ Vechicle class, use to create vehicle instance """

    vehicle_type = ['two_wheeler', 'four_wheeler']

    def __new__(cls, v_type, registration):
        if v_type not in cls.vehicle_type:
            print("Oops vehicle type not correct")
        else:
            print("Creating vehicle ")
            return object().__new__(cls)

    def __init__(self, v_type, registration):
        self.v_type = v_type
        self.registration = registration


# v = Vehicle('two_wheeler', 123456)

# print(vars(v))

# print(v.v_type)
