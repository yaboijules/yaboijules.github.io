import math

class Circle:
	#adding a doc string is brought up when you use help(class_name)
	"""This is a circle class, whaddup
	Test test test test test hahaha yes"""

	#initializer
	def __init__(self, radius): #instance variable
		self.__radius = radius #making it self.__radius makes it private. 
		#this attribute can now only be accessed by methods within the class,
		#someone who does circle.__radius will get an error.

	def get_area(self): #instance method
		"""returns the area of the circle"""
		return math.pi *self.__radius**2 

	def get_perimeter(self): #instance method
		"""returns the perimeter of the circle"""
		return 2 * math.pi * self.__radius

	def get_radius(self):
		"""returns the radius of the circle"""
		return self.__radius

	def set_radius(self, radius): #this makes it so you can only assign ints to __radius
		"""reassigns radius attribute, makes sure it is an int"""
		if not isinstance(radius, int):
			print("Error: "+radius+" is not an int")
			return
		self.__radius = radius
		

my_circle = Circle(15)
print(my_circle.get_area())
print(my_circle.get_perimeter())

c1 = Circle(69)
c2 = Circle(420)

def print_circle_info(obj):
	print('-'*40)
	print('Radius of circle: ', format(obj.get_radius(), '.2f'))
	print('Perimeter of circle: ', format(obj.get_perimeter(), '.2f'))
	print('Area of circle: ', format(obj.get_area(), '.2f'))
	print('-'*40)

print_circle_info(c1)
print_circle_info(c2)


#this is a cool thing, lets you know all the shit in the class
help(Circle)



input()