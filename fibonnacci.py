def memoize_factorial(f): 
    memory = {} 
  
    # This inner function has access to memory 
    # and 'f' 
    def inner(num): 
        print("inner",num)            
        if num not in memory:          
            memory[num] = f(num) 
            print("put into",num,memory[num])            

        else:
            print('get from memery:',num,memory[num])            
        return memory[num] 
  
    return inner 

@memoize_factorial      
def fibonnacci(n):
    print('calculating: ', n)
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonnacci(n-2)*fibonnacci(n-1)

print(fibonnacci(10))