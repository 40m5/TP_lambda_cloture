def create_multiplier(n):
    return lambda x: x * n


double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  
print(triple(5))  


print(double(10))  
print(triple(7))   
print(double(3))   
print(triple(2))  



