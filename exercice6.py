def filterMap(filter_func, map_func, lst):
    return [map_func(x) for x in lst if filter_func(x)]


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_mapped = filterMap(lambda x: x % 2 == 0, lambda x: x ** 2, numbers)

print(filtered_mapped)  

words = ["hello", "", "world", "python", "", "lambda"]
filtered_transformed = filterMap(lambda x: x != "", lambda x: x.upper(), words)

print(filtered_transformed) 
