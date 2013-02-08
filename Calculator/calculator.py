#Basic calculator project
import math
def cube(n):
    """
    Return the cube of a number, an integer provided as 'n'
    """
    return pow(n,3)

def squareroot(n):
    """
    Returns the square root of the number n. If n < 0, 
    then return the string "NAN" (Not A Number)
    """
    return pow(n, 0.5)

def negate(n):
    """ Return the negative value of the argument 'n'.
    """
    return 0-n

def factorial(n):
    """Return n factorial
    The factorial of anything <= 1 is 1.
    The factorial of any integer greater than 1 is the product of all
    the integers from 1 to the number itself. For example,
    4 factorial = 1 x 2 x 3 x 4 = 24.
    """
    facto = 1
    while (n > 0):
        facto *= n
        n-=1
    return facto
