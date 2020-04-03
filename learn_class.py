#__ is private member
class MyClass: 
    # Hidden member of MyClass 
    def __init__(self):
        self.__hiddenVariable = 0
    
    # A member method that changes  
    # __hiddenVariable  
    def add(self, increment): 
        self.__hiddenVariable += increment 
        print (self.__hiddenVariable) 

    def __str__(self):
        return 'this is me'
    def __repr__(self):
        return 'this is me for dev'
# Driver code 
myObject = MyClass()      
myObject.add(2) 
myObject.add(5) 
print(myObject) 
print([myObject]) 
# Inheritance
# isinstance
# issuperclass

# A Python program to demonstrate inheritance  
  
# Base or Super class. Note object in bracket. 
# (Generally, object is made ancestor of all classes) 
# In Python 3.x "class Person" is  
# equivalent to "class Person(object)" 
class Person(object): 
      
    # Constructor 
    def __init__(self, name): 
        self.name = name 
  
    # To get name 
    def getName(self): 
        return self.name 
  
    # To check if this person is employee 
    def isEmployee(self): 
        return False
  
  
# Inherited or Sub class (Note Person in bracket) 
class Employee(Person): 
  
    # Here we return true 
    def isEmployee(self): 
        return True
  
# Driver code 
emp = Person("Geek1")  # An Object of Person 
print(emp.getName(), emp.isEmployee()) 
  
emp = Employee("Geek2") # An Object of Employee 
print(emp.getName(), emp.isEmployee())

# Class for Computer Science Student 
class CSStudent: 
    stream = 'cse'     # Class Variable  
    def __init__(self, name, roll): 
        self.name = name  
        self.roll = roll 
  
# Driver program to test the functionality 
# Creating objects of CSStudent class 
a = CSStudent("Geek", 1) 
b = CSStudent("Nerd", 2) 
  
print ("Initially")
print ("a.stream =", a.stream )
print ("b.stream =", b.stream )
  
# This thing doesn't change class(static) variable 
# Instead creates instance variable for the object 
# 'a' that shadows class member. 
CSStudent.stream = "ece"
  
print ("\nAfter changing a.stream")
print ("a.stream =", a.stream )
print ("b.stream =", b.stream )

num = 23
print("Type of num is:", type(num)) 
  
lst = [1, 2, 4] 
print("Type of lst is:", type(lst)) 
  
name = "Atul"
print("Type of name is:", type(name)) 