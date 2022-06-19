class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price, power):
        self.make = make
        self.price = price
        self.power = power
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99, 1.5)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.99
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.99, 2.0)
print(hamilton.make)
print(hamilton.price)
print(hamilton.power)

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
Kettle.switch_on(kenwood)

print("*" * 80)

print("Switch to atomic power!")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print("Now switch to gas power!")
Kettle.power_source = "gas"
print(Kettle.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)