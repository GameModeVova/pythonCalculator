#BELOW ARE INDIVIDUAL MATH FUNCTIONS
import math

def add(first_value, second_value):
    return(round(float(first_value)+float(second_value),10))

def sub(first_value, second_value):
    return(round(float(first_value)-float(second_value),10))

def mul(first_value, second_value):
    return(round(float(first_value)*float(second_value),10))

def div(first_value, second_value):
    zero_div_error = "YOU HAVE COMMITED A SIN BY ATTEMPTING TO DIVIDE BY ZERO" #Change this error message to something actually meaningful
    
    #CHECKING FOR DIVISION BY ZERO
    if second_value == 0:
        return(zero_div_error)
    else:
        return(round(float(first_value)/float(second_value),10))

def exp(first_value, second_value): 
    return(round(math.pow(float(first_value), float(second_value)),10))

def root(first_value, second_value):
    return(round(math.pow(float(second_value), 1/(float(first_value))),10))

def fact(first_value):
    non_integer_error = "YOU HAVE SINNED BY ATTEMPTING TO CALCULATE FACTORIAL OF A NON-INTEGER" #This error message should also be changed

    if first_value.is_integer():
        return(round(math.factorial(int(first_value)),10))
    else:
        return(non_integer_error)

def mod(first_value, second_value):
    div_error = "YOU HAVE COMMITED A SIN BY ATTEMPTING TO DIVIDE BY ZERO" #Change this error message to something actually meaningful
    
    #CHECKING FOR DIVISION BY ZERO
    if second_value == 0:
        return(div_error)
    else:
        return(round(float(first_value)%float(second_value),10))
