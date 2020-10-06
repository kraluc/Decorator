#!/bin/env python

""" We have to weigh quantities (e.g. sugar or flour) from 1 to 40 pounds. What is the least number of weights that can be used on a balance scale to way any of these quantities

assume that weight can be placed on either side of the scale

assume that only one instance of a weight is available

Un-used weights
weight with DUT
weight alone

Minimal combination = Set size
Individual weight < 40 lbs


"""


### first approach based on lists does not keep track of the weights used to compute the sums

def unique(list1):
    result = []
    while list1:
        last = list1.pop()
        if last not in result:
            result.append(last)
    return sorted(result)

a = [1, 2, 1, 4]

print(f'unique version of {a} is {unique(a)}')


def merge(list1, list2):
    return unique(list1 + list2)

b = [1, 2, 5, 6]
c = [3, 2, 8, 6]

print(f'merged {b} and {c} = {sorted(merge(b,c))}')


def scalar_plus_list(number:int, my_list:list)->list:
    result = []
    for item in my_list:
        result.append(number + item)
    return result

print(f'list {b} + number 12 is {scalar_plus_list(12,b)}')


def sums(my_list:list)->list:
    """ returns a list that includes all possible sums among elements of my_list """
    if my_list:
        # pop the last element
        last = my_list.pop()
        # Sum (n) = Last(n) + list of ones x last(n) +  Sum(n-1) + Sum(n-1)
        sub_sum = sums(my_list)
        cross = scalar_plus_list(last, sub_sum)
        return unique([ last, ] + cross + sub_sum)
    else:
        return []

a = list(range(1,11))

print(f'for list {a}')
result = sums(a)

print(f'all possible sums are: {result}')
print(f'length is {len(result)}')

def factors_set():
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    yield (i, j, k, l)


def memoize(f):
    results = {}
    def helper(n):
        if n not in results:
            results[n] = f(n)
        return results[n]
    return helper


@memoize
def linear_combinations(n):
    """returns the tuple (i, j, k, l) satisfying
       n = i * 3^0 + j* 3^1 + k * e^2 + l * 3^3  """
    weights = (1, 3, 9, 27)

    for factors in factors_set():
        sum = 0
        for i in range(len(factors)):
            sum += factors[i] * weights[i]
        if sum == n:
            return factors


# calculate the linear combinations of the first 10 positive integers:
for i in range(1, 11):
    print(linear_combinations(i))

