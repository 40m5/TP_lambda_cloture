def compose(f, g):
    return lambda x: f(g(x))


double = lambda x: x * 2
increment = lambda x: x + 1

double_after_increment = compose(double, increment)
print(double_after_increment(5))  

square = lambda x: x ** 2
halve = lambda x: x / 2

square_then_halve = compose(halve, square)
print(square_then_halve(4)) 
print(square_then_halve(10)) 
