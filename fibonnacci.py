def memoize_factorial(f): 
    memory = {} 
  
    # This inner function has access to memory 
    # and 'f' 
    def inner(num): 
        print(num)            
        if num not in memory:          
            print('put into memery:',num)            
            memory[num] = f(num) 
        else:
            print('get from memery:',num)            
        return memory[num] 
  
    return inner 

@memoize_factorial      
def fibonnacci(n):
    print('calculating: ', n)
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonnacci(n-1)+fibonnacci(n-1)

print(fibonnacci(10))