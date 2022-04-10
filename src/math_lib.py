##
# @file math_lib.py
# @brief Library for basic mathematical functions. 
# Library for mathematical functions that includes multiplication, 
# addition, substraction, division, modulo, exponentiation, n-th root
# and factorial.

# Imports
import math


def add(first_value, second_value):
    """! Adds 2 numbers.

    @param first_value      The first summand.
    @param second_value     The second summand.

    @return                 Sum of summands represented by float number rounded by 10 decimal places.
    """
    return(round(float(first_value)+float(second_value),10))

def sub(first_value, second_value):
    """! Substracts 2 numbers.

    @param first_value      Minuend.
    @param second_value     Subtrahend.

    @return                 Difference between minuend and subtrahend represented by float number rounded by 10 decimal places.
    """
    return(round(float(first_value)-float(second_value),10))

def mul(first_value, second_value):
    """! Multiplies 2 numbers.

    @param first_value      The first factor.
    @param second_value     The second factor. 

    @return                 Product of factors represented by float number rounded by 10 decimal places.
    """


    return(round(float(first_value)*float(second_value),10))

def div(first_value, second_value):
    """! Divides first number by the second. Will raise an expection in case of dividing by zero. 

    @param first_value      Divident.
    @param second_value     Divisor. 

    @return                 Quotient represented by float number rounded by 10 decimal places.
    """
    try:
        return(round(float(first_value)/float(second_value),10))
    except: 
        Exception

def exp(first_value, second_value): 
    """! Exponentiates first number to the second number. 

    @param first_value      Base.
    @param second_value     Exponent. 

    @return                 Power represented by float number rounded by 10 decimal places.
    """
    return(round(math.pow(float(first_value), float(second_value)),10))

def root(first_value, second_value):
    """! Calculates n-th root of the first number. Degree is determined by the second number. 

    @param first_value      Radicant.
    @param second_value     Degree. 

    @return                 Root represented by float number rounded by 10 decimal places.
    """
    try:
        return(round(first_value**(1/second_value),10))
    except:
        Exception

def fact(first_value):
    """! Calculates the factorial of the number. 

    @param first_value      Radicant.
    @param second_value     Degree. 

    @return                 Product represented by an integer number.
    """
    try: 
        return(math.factorial(int(first_value)))
    except:
        Exception

def mod(first_value, second_value):
    """! Calculates remainder (modulo) after the first number divided by the second number. 

    @param first_value      Divident.
    @param second_value     Divisor. 

    @return                 Remainder represented by float number rounded by 10 decimal places.
    """
    try: 
        return(round(float(first_value)%float(second_value),10))
    except:
        Exception
    
### End of file math_lib.py ###