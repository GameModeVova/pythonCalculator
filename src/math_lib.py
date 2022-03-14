import math
import numpy as np

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
    try:
        return(round(first_value**(1/second_value),10))
    except:
        Exception

"""    complex_root_error = "ERROR MESSAGE" #change this to a meaningful error message
    zero_root_error = "ERROR MESSAGE" #change this to a meaningful error message
    negative_rooter_zero_root_error = "ERROR MESSAGE" #change this to a meaningful error message --- might also want to change the name

    #CHECKING FOR ROOT BY ZERO
    if second_value != 0:
        #CHECKING FOR IMAGINARY NUMBER ERROR
        if np.iscomplex(round(first_value**(1/second_value),10)):
            return(complex_root_error)
        else:
            return(round(first_value**(1/second_value),10))
    elif second_value == 0 and first_value == 1:
        #CHECKING FOR IMAGINARY NUMBER ERROR
        if np.iscomplex(round(first_value**(0),10)):
            return(complex_root_error)
        else:
            return(round(first_value**(0),10))
    elif first_value == 0 and second_value < 0:
        return(negative_rooter_zero_root_error)
    else:
        return(zero_root_error)
"""   

def fact(first_value):
    non_integer_error = "YOU HAVE SINNED BY ATTEMPTING TO CALCULATE FACTORIAL OF A NON-INTEGER" #This error message should also be changed

    if float(first_value).is_integer():
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
