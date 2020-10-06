#!/bin/env python
import sys

def validate_int(func):
    def wrapper(*args):
        incorrect_types = {}
        for arg in args:
            variable_type = type(arg)
            print(f'variable type {variable_type}')
            if variable_type != type(1):
                if variable_type in incorrect_types:
                    incorrect_types[variable_type].append(arg)
                else:
                    incorrect_types[variable_type] = [arg,]

        if incorrect_types:
            print('Aborting: input variable(s) should all be integers')
            print(f'the following variables are not: {incorrect_types}')
            sys.exit(1)
        else:
            return func(*args)
    return wrapper


@validate_int
def is_greater(a, b):
    # returns True if 'a' is greater
    if a < b:
        return False
    return True




if __name__ == "__main__":
    # output is 'True'
    print(is_greater(5, 5))
    # TypeError
    print(is_greater(5, "four"))