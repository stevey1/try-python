# Python program to demonstrate  
# use of class method and static method. 
from datetime import date 
  
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
        self.say_hi()
    def say_hi(self): 
        print('Hello, my name is', self.name)  
    # a class method to create a Person object by birth year. 
    @classmethod
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 
      
    # a static method to check if a Person is adult or not. 
    @staticmethod
    def isAdult(age): 
        return age > 18
    age = 25    
    def printAge(cls):
        print('The age is:', end='')        
        print (cls.age)
  
person1 = Person('mayank', 21) 
person2 = Person.fromBirthYear('mayank', 1996) 
  
print (person1.age)
print (person2.age )
  
# print the result 
print (Person.isAdult(22) )
Person.printAge = classmethod(Person.printAge)
Person.printAge()