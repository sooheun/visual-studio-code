n, k = map(int, input("").split())

def power(a, n):
    
    result = 1
    
    while n:
        
        if n&1:
            
            result *= a
        
        a *= a
        
        n = n>>1
    
    return result


print(power(3, 10))