import math
<<<<<<< Updated upstream
import numpy as np
=======
>>>>>>> Stashed changes

def add(first_value, second_value):
    return(round(float(first_value)+float(second_value),10)) #won't be better

def sub(first_value, second_value):
    return(round(float(first_value)-float(second_value),10)) #won't be better

def mul(first_value, second_value):
    return(round(float(first_value)*float(second_value),10)) #won't be better

def div(first_value, second_value): #probably perfect
    zero_div_error = "error: division by zero" 
    
    #CHECKING FOR DIVISION BY ZERO
    if second_value == 0:
        return(zero_div_error)
    else:
        return(round(float(first_value)/float(second_value),10))

def exp(first_value, second_value): 
    return(round(math.pow(float(first_value), float(second_value)),10))

def root(first_value, second_value): #I am not sure if this is working fine
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

def fact(first_value): #probably fine
    non_integer_error = "error: factorial of a non-integer" 

    if float(first_value).is_integer():
        return(round(math.factorial(int(first_value)),10))
    else:
        return(non_integer_error)

def mod(first_value, second_value): #probably fine
    div_error = "error: division zero" 
    
    #CHECKING FOR DIVISION BY ZERO
    if second_value == 0:
        return(div_error)
    else:
        return(round(float(first_value)%float(second_value),10))
