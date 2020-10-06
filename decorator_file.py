#!/bin/env python

from functools import wraps

### Wraps re-assign the doc-string, function-name to decorated function
def greeting(func):
    @wraps(func)
    def function_wrapper(x):
        """function wrapper of greeting"""
        print("Hi, " + func.__name__ + " returns:")
        return func(x)
    return function_wrapper

def memoize(f):
    """ cache computed values for re-use """
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib(n):
    """Compute Fibonacci element"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(f'\nFibonacci(40): {str(fib(40))}\n')

def f(x):
    def g(y):
        return y + x + 3
    return g

nf1 = f(1) # this is a function
nf2 = f(3) # this is also a function

print(nf1(1)) # this is a value returned by the function nf1 for input 1
print(nf2(1))

@greeting
def greeting_func_gen(lang):
    def customized_greeting(name):
        if lang == "de":    # German
            phrase = "Guten Morgen "
        elif lang == 'fr':  # French
            phrase = "Bonjour "
        elif lang == "it":  # Italian
            phrase = "Buongiorno "
        elif lang == "sp":  # Spanish
            phrase = "Buenos Dias "
        elif lang == "tr":  # Turkish
            phrase = "Günaydin "
        elif lang == "gr":  # Greek
            phrase = "Καλημερα "
        else:
            phrase = "Hi "
        return phrase + name + "!"
    return customized_greeting

say_hi = greeting_func_gen("tr")
print(say_hi("Gülay"))  # This Turkish name means "rose moon" by the way
say_hi = greeting_func_gen("fr")
print(say_hi("Vincent"))







def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x**2 + b * x + c
    return polynomial

p1 = polynomial_creator(2, 3, -1)
p2 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2, 1):
    print(x, p1(x), p2(x))


def polynomial_creator(*coeffs):
    """coefficients are in the form a_n, ..., a_1, a_0
    """
    def polynomial(x):
        res = coeffs[0]
        for i in range(1, len(coeffs)):
            res = res * x + coeffs[i]
        return res
    return polynomial

p1 = polynomial_creator(4)
p2 = polynomial_creator(2, 4)
p3 = polynomial_creator(1, 8, -1, 3, 2)
p4 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2, 1):
    print(x, p1(x), p2(x), p3(x), p4(x))

def our_decorator(func):
    def functional_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return functional_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))

foo("Hi")



def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper

@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

for i in range(1, 10):
    print(i, factorial(i))

print(factorial(-1))

'''
def call_counter(func):
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0
    return helper

@call_counter
def succ(x):
    return x + 1

print(succ.calls)
for i in range(10):
    succ(i)

print(succ.calls)
'''

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0

    return helper

@call_counter
def succ(x):
    return x + 1

@call_counter
def mull(x, y=1):
    return x*y + 1

print(succ.calls)
for i in range(10):
    succ(i)
mull(3, 4)
mull(4)
mull(y=3, x=2)

print(f'successor calls {succ.calls:>10}')
print(f'multiplier calls {mull.calls:>9}')