"""Inheritance

Create a base class called Shape with a method calculateArea().
 Derive two classes Rectangle and Circle from Shape. 
 Implement the calculateArea() method in each derived class to calculate the area of the rectangle and circle,
  respectively.

Create a base class called Animal with properties name and sound and a method makeSound(). 
Derive two classes Cat and Dog from Animal. Implement the makeSound() method in each derived class to 
print the specific sound made by a cat or dog.

Create a base class called Person with properties name and age. Derive a class Student from Person 
with an additional property grade. Implement a method displayInfo() in the Person class to display the name and age,
 and override the displayInfo() method in the Student class to display the name, age, and grade.

Create a base class called Employee with properties name and salary. Derive two classes Manager and Developer from 
Employee. Implement a method calculateBonus() in each derived class to calculate the bonus based on the salary. 
The Manager class should have a higher bonus percentage than the Developer class."""

class shape:
    def  calculateArear(self,l,b):
        self.l=l
        self.b=b
        print(2*(self.l*self.b))

    def calculateAreac(self,r):
        self.r=r
        print(2*3.142*self.r*self.r)
            
class rectangle(shape):
    print("This is the Area of Rectangle")
    
class circle(shape):
    print("This is the Area of Circle")

r=rectangle()
r.calculateArear(5,8)

c=circle()
c.calculateAreac(5)
#=======================================================================================================================
"""Create a base class called Vehicle with properties color and fuelType and a method startEngine().
 Derive two classes Car and Motorcycle from Vehicle. Implement the startEngine() method in each derived class 
 to print a message indicating the vehicle type and engine start."""

class vehicle:
    color="Dark Black"
    fueltype="Petrol"
    def startengine(self):
       print("This is the colour :",self.color,"& This is the Fueltype :",self.fueltype)

class car(vehicle):
    print("")

class Motorcycle(vehicle):
    print("")

c=car()
c.startengine()

m=Motorcycle()
m.startengine()
#=======================================================================================================================
"""Create a base class called Animal with properties name and sound and a method makeSound(). 
Derive two classes Cat and Dog from Animal. Implement the makeSound() method in each derived class to 
print the specific sound made by a cat or dog."""

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def makeSound(self):
        print(f"{self.name} makes {self.sound} sound")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "meow")
    def makeSound(self):
        print(f"{self.name} makes {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "bark")
    def makeSound(self):
        print(f"{self.name} makes {self.sound}")

cat = Cat("Whiskers")
dog = Dog("Buddy")

cat.makeSound()
dog.makeSound()

