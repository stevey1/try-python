# can be treated as objects 
def shout(text): 
    return text.upper() 
yell = shout 
print (yell('Hello'))

  
# def whisper(text): 
def whisper(text): 
    return text.lower() 
def greet(f): 
    print (f("Hi, I am created by a function passed as an argument.") )
  
greet(shout) 
greet(whisper) 


# Functions can return another function 
  
def create_adder(x): 
    def adder(y): 
        return x+y 
  
    return adder 
  
add_15 = create_adder(15)
print(add_15(2))