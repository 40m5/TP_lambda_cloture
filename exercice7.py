import time


def memoize(func):
    cache = {}

    def memorized_func(x):
        if x in cache:
            return cache[x]
        else:
            result = func(x)
            cache[x] = result
            return result

    return memorized_func


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


memoized_factorial = memoize(factorial)
memoized_fibonacci = memoize(fibonacci)


start = time.time()
print(memoized_fibonacci(35))  
print("Temps d'exécution :", time.time() - start, "secondes")

start = time.time()
print(memoized_factorial(10))  
print("Temps d'exécution :", time.time() - start, "secondes")

