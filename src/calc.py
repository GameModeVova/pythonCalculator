import math
import math_lib 

#IMPORTANT check for division by zero

#HELPER --- missing help message, might be better to do alongside GUI
def help_initiator(user_input):
    helper =  "HERE YOU WILL HAVE A TEXT TRYING TO HELP A USER WHO GOT LOST"
    if user_input == "?":
        return(help)
    
#ERRORCHECKER --- missing check for few errors (vis. inside function)
def error_checker(user_input):
    error = "HERE YOU WILL HAVE A TEXT CONVEYING TO THE USER THAT HE HAS DONE BIG BAD"
    
    allowed_numerics = "0123456789."
    allowed_operators = "+-*/!^%√" #specific case for !, where user inputs only one number

    #
    # MISSING AN ERROR FOR INCORRECT POSITIONING OF INPUT ex.: "^23-*2*", ban such format as an input in GUI
    #

    for i in user_input:
        if (i in allowed_numerics) or (i in allowed_operators):
            return(user_input)
        else:
            return(error)
    
#FORMATING USER INPUT INTO A FORM SUITABLE FOR THE PROGRAM --- SHOULD BE ALL SET
def input_formating(user_input):
    allowed_operators = "+-*/!^%√"
    operator = ""
    #checking if the first number is negative or positive
    if user_input[0] == "-":
        user_input = user_input.replace("-", "n", 1) #temporarily replaces first number's sign for convinience
    
    for i in user_input: #this will select the operation
        if i in allowed_operators:
            operator = i
            break
    
    user_input = user_input.split(operator, 1) #now formatted version is as follows: [first_number(still with 'n' instead of '-'), second_number(this one retained its sign))]

    #giving back '-' to first_number, if it is negative
    if user_input[0][0] == "n":
        user_input[0] = user_input[0].replace("n", "-", 1)
    
    user_input.append(operator)
    
    return(user_input) #format of this is: [0 = first number, 1 = second number, 2 = operator] ***for some functions, len(user_input_list) == 2, omitting the second number

#CHOOSING A FUNCTION TO EXECUTE --- NEEDS HEAVY REWORK, FUNCTION SPLIT CAN BE DONE AUTOMATICALLY AND NOT MULTIPLE TIMES
def function_executioner(user_input):
    #ADDITION
    if user_input[-1] == "+":
        return(math_library.addition(user_input[0], user_input[1]))

    #SUBTRACTION
    if user_input[-1] == "-":
        return(math_library.subtraction(user_input[0], user_input[1]))
    
    #MULTIPLICATION
    if user_input[-1] == "*":
        return(math_library.multiplication(user_input[0], user_input[1]))
    
    #DIVISION
    if user_input[-1] == "/":
        return(math_library.division(user_input[0], user_input[1]))

    #EXPONENT
    if user_input[-1] == "^":
        return(math_library.exponent(user_input[0], user_input[1]))

    #ROOT
    if user_input[-1] == "√":
        return(math_library.root(user_input[0], user_input[1]))
    
    #FACTORIAL
    if user_input[-1] == "!":
        return(math_library.factorial(user_input[0]))

    #REMAINDER
    if user_input[-1] == "%":
        return(math_library.remainder(user_input[0], user_input[1]))

#ADDING ALL FUNCTIONS FOR A RESULT, ALSO SAVES RESULT INTO CASHE
def solver(user_input):
    return(function_executioner(input_formating(error_checker(user_input))))
