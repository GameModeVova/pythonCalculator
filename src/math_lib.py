#BELOW ARE INDIVIDUAL MATH FUNCTIONS
import math

def add(first_value, second_value):
    return(float(first_value)+float(second_value))

def sub(first_value, second_value):
    return(float(first_value)-float(second_value))

def mul(first_value, second_value):
    return(float(first_value)*float(second_value))

def div(first_value, second_value):
    return(float(first_value)/float(second_value))

def exp(first_value, second_value): 
    return(math.pow(float(first_value), float(second_value)))

def root(first_value, second_value):
    return(math.pow(float(second_value), 1/(float(first_value))))

def fact(first_value):
    return(math.factorial(int(first_value)))

def mod(first_value, second_value):
    return(float(first_value)%float(second_value))