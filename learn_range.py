import sys 
  
# initializing a with range() 
a = range(1,10000) 
  
 
print (a) 
# testing the size of a 
# range() takes more memory 
print ("The size allotted using range() is : ") 
print (sys.getsizeof(a)) 
  

def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
for b in simpleGeneratorFun():
    print(b)

