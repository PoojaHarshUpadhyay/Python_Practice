fib_cache = {}

def fibo(n):
    if(n == 1):
        value = 1
    elif (n == 2):
        value = 1
    elif (n > 2): 
        value = fibo(n-1) + fibo(n-2)
    fib_cache[n] = value
    return value
    
for n in [1, 100]:
    print(n , ":", fibo(n))
    
