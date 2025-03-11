# Exercise 1: Basic Calculator Functions
from typing import Union

# Defining a Number type for cleaner type hints
Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    
    result = a + b
    return result
    
def subtract(a: Number, b: Number) -> Number:
    result = a-b
    return result

def multiply(a: Number, b: Number) -> Number:
    result = a*b
    return result

def divide(a: Number, b: Number) -> Number:
    result = a/b
    return result

    



