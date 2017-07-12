class Kettle(object):

    power_source = 'electricity'

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

Kenwood = Kettle("kenwood", 8.25)
print(Kenwood.make)
print(Kenwood.price)

Kenwood.price = 12.89
print(Kenwood.price)

Hamilton = Kettle("Hamilton", 7.90)
print(Hamilton.make)
print(Hamilton.price)

print("Models : {} = {} {} = {}".format(Kenwood.make, Kenwood.price, Hamilton.make, Hamilton.price))

print("Models : {0.make} = {0.price} {1.make} = {1.price}".format(Kenwood, Hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""

print(Hamilton.on)
Hamilton.switch_on()
print(Hamilton.on)

Kettle.switch_on(Kenwood)
print(Kenwood.on)

print("*" * 80)

Kenwood.power = 1.5
print(Kenwood.power)
#print(Hamilton.power)

print("Switch kettel power source to atomic")
Kettle.power_source='atomic'
print(Kettle.power_source)
print("Switch Kenwood powersoure to gas")
Kenwood.power_source='gas'
print(Kenwood.power_source)
print(Hamilton.power_source)
print(Kettle.__dict__)
print(Kenwood.__dict__)
print(Hamilton.__dict__)
