square = lambda x: x ** 2
print(square(5))  

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  

sum_lambda = lambda a, b: a + b
print(sum_lambda(3, 7))  

from functools import reduce

numbers = [1, 2, 3, 4, 5]
total_sum = reduce(lambda a, b: a + b, numbers)
print(total_sum)  






