# let's define the class bike
class Bike:
    def __init__(self, color, frame_material):
        self.color = color
        self.frame_material = frame_material

    def brake(self):
        print("Breaking!")

# let's create a couple of instances
red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')

# let's inspect the object we have, instance of the Bike class
print(red_bike.color)
print(red_bike.frame_material)
print(blue_bike.color)
print(blue_bike.frame_material)

# let's brake!
red_bike.brake()

'''
Notes:
__init__ -> initializer method - it sets up the objects with the values we pass when we create it. In Python, double underscore before methods is called magic method. Is is used for different purposes. We never name things this way. Let's leave it for Python, shall we?

brake() is an additional method.

The set of attributes of an object is considered to be a namespace. By getting to the frame_type property through different namespace (red_bike, blue_bike) we obtain different values.

The dot (.) is the means we use to walk into a namespace. 
'''