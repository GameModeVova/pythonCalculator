#BELOW ARE INDIVIDUAL MATH FUNCTIONS
import math

def add(first_value, second_value):
    return(round(float(first_value)+float(second_value)), 10)

def sub(first_value, second_value):
    return(round(float(first_value)-float(second_value)), 10)

def mul(first_value, second_value):
    return(round(float(first_value)*float(second_value)), 10)

def div(first_value, second_value):
    return(round(float(first_value)/float(second_value)), 10)

def exp(first_value, second_value): 
    return(round(math.pow(float(first_value), float(second_value))), 10)

def root(first_value, second_value):
    return(round(math.pow(float(second_value), 1/(float(first_value)))), 10)

def fact(first_value):
    return(round(math.factorial(int(first_value))), 10)

def mod(first_value, second_value):
    return(round(float(first_value)%float(second_value)), 10)
