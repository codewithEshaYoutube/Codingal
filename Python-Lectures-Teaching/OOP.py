class Parrot: # parent
  #attributes
  specie="Birds"

  # adding instance attributes
  def __init__(self,name,age):
    # binding of attributes
    self.name=name
    self.age=age
# instantiate of class Parrot ( objects)
#child
blu=Parrot("Blu",10)
woo=Parrot("woo",15)
# calling the object attributes
print(f"Blu is a {blu.specie}")
print(f"Blu is  {blu.age} years old")
print(f"Woo is a {woo.specie}")
print(f"Woo is  {woo.age} years old")

print(f"Blu is a {blu.specie}")
print(f"Blu is  {blu.age}years old")
#making the class
class Vehicle:
  def __init__(self,max_speed,mileage):
    # binging the arguments
    self.max_speed=max_speed
    self.mileage=mileage
  #creating class
Bus=Vehicle(120,18)
Car=Vehicle(240,30)
print("This is the mileage of bus",Bus.mileage)
print("this the mileage of car. ",Car.mileage)
class Fruit:
   def __init__(self,name,color,taste):
    self.name=name
    self.color=color
    self.taste=taste

apple=Fruit("Apple","Red","sweet")# child -parent relationship
banana=Fruit("banana","yellow","sweet")# child -parent relationship
orange=Fruit("orange","orange","citrus")# child -parent relationship

# calling our object
print(apple.color)

print(banana.name)
print(orange.color)
print(orange.taste)
print(apple.taste)

class Student:
    def __init__(self, name):
        self.name = name
        self.__hours = 0  # hidden property

    def study(self, hrs):
        self.__hours += hrs

    def progress(self):
        print(f"{self.name} studied for {self.__hours} hours in total")


student1 = Student("Esha")
student1.study(6)
student1.study(8)
student1.progress()

class Student:
    def __init__(self, name):
        self.name = name
        self.__hours = 0   # hidden detail

    def study(self, hrs):
        self.__hours += hrs

    def progress(self):
        print(f"{self.name} studied {self.__hours} hours total.")

# Using abstraction
s1 = Student("Esha")
s1.study(3)
s1.study(2)  
s1.progress()
class Overload():
  def __init__(self,real,image):
    self.real=real
    self.image=image
  def __add__(self,other):
    return Overload(self.real+other.real,self.image+other.image)
  def __str__(self):
    return f"{self.real}+{self.image}i"
# making instances (objects)

c1=Overload(3,4)
c2=Overload(7,8)
c3=Overload(17,8)
c4=Overload(7,5)
c5=Overload(7,98)
c7=Overload(19,8)

print(c1+c2+c3+c4+c5+c7)

