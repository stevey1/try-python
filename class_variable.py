class ClassVariable: 
    count = 0     # class attribute 
    def __init__(self):
        self.increase()
    def increase(self): 
        ClassVariable.count += 1
  
# Calling increase() on an object 
s1 = ClassVariable() 
print (s1.count)
  
# Calling increase on one more 
# object 
s2 = ClassVariable() 
print (s2.count )
  
print (ClassVariable.count)