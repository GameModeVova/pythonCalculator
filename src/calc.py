import math
import math_lib
import tkinter as tk

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
        return(math_lib.addition(user_input[0], user_input[1]))

    #SUBTRACTION
    if user_input[-1] == "-":
        return(math_lib.subtraction(user_input[0], user_input[1]))
    
    #MULTIPLICATION
    if user_input[-1] == "*":
        return(math_lib.multiplication(user_input[0], user_input[1]))
    
    #DIVISION
    if user_input[-1] == "/":
        return(math_lib.division(user_input[0], user_input[1]))

    #EXPONENT
    if user_input[-1] == "^":
        return(math_lib.exponent(user_input[0], user_input[1]))

    #ROOT
    if user_input[-1] == "√":
        return(math_lib.root(user_input[0], user_input[1]))
    
    #FACTORIAL
    if user_input[-1] == "!":
        return(math_lib.factorial(user_input[0]))

    #REMAINDER
    if user_input[-1] == "%":
        return(math_lib.remainder(user_input[0], user_input[1]))

#ADDING ALL FUNCTIONS FOR A RESULT, ALSO SAVES RESULT INTO CASHE
def solver(user_input):
    return(function_executioner(input_formating(error_checker(user_input))))

#Basic tkinter UI Layout
#---------------------------------------------------------------------------

#WINDOW CONFIG
window = tk.Tk()
window.title("Calculator")
window.geometry("720x800")

#PLACEMENT GRID CONFIG
window.columnconfigure((0,4,7),weight=1)
window.columnconfigure((1,2,3,5,6),weight=3)

window.rowconfigure((0,2,7,9),weight=1)
window.rowconfigure((1,8), weight = 2)
window.rowconfigure((3,4,5,6), weight=3)

#WINDOW MENU
head_menu = tk.Menu(window)

help_menu = tk.Menu(head_menu, tearoff=0)
help_menu.add_command(label="+")
help_menu.add_command(label="-")
help_menu.add_command(label="*")
help_menu.add_command(label="/")
help_menu.add_command(label="^")
help_menu.add_command(label="√")
help_menu.add_command(label="!")
help_menu.add_command(label="%")
head_menu.add_cascade(label="Help", menu=help_menu)

theme_menu = tk.Menu(head_menu, tearoff=0)
head_menu.add_cascade(label="Theme", menu=theme_menu)

window.config(menu=head_menu)

#DISPLAY
# functions
# ---------------------------------------------------------------------------------------------------------------------------
current_val = ""

def click_clear():
    global current_val
    current_val = ""
    d_num.set(current_val)

def click_delete():
    global current_val
    current_val = current_val[0:-1]
    d_num.set(current_val)

# key entry
def click_1():
    global current_val
    current_val = current_val + "1"
    d_num.set(current_val)


def click_2():
    global current_val
    current_val = current_val + "2"
    d_num.set(current_val)


def click_3():
    global current_val
    current_val = current_val + "3"
    d_num.set(current_val)


def click_4():
    global current_val
    current_val = current_val + "4"
    d_num.set(current_val)


def click_5():
    global current_val
    current_val = current_val + "5"
    d_num.set(current_val)


def click_6():
    global current_val
    current_val = current_val + "6"
    d_num.set(current_val)


def click_7():
    global current_val
    current_val = current_val + "7"
    d_num.set(current_val)


def click_8():
    global current_val
    current_val = current_val + "8"
    d_num.set(current_val)


def click_9():
    global current_val
    current_val = current_val + "9"
    d_num.set(current_val)


def click_0():
    global current_val
    current_val = current_val + "0"
    d_num.set(current_val)

# label
# ---------------------------------------------------------------------------------------------------------------------------
d_num = tk.StringVar(window)
d_num.set(current_val)
display = tk.Label(window,textvariable=d_num)
display.grid(row=1,column=0,columnspan=7,ipady=20,ipadx=720)

#NUMPAD
key_1 = tk.Button(window,text="1",command=click_1).grid(row=3,column=1,ipady =40,ipadx=40)
key_2 = tk.Button(window,text="2",command=click_2).grid(row=3,column=2,ipady =40,ipadx=40)
key_3 = tk.Button(window,text="3",command=click_3).grid(row=3,column=3,ipady =40,ipadx=40)
key_4 = tk.Button(window,text="4",command=click_4).grid(row=4,column=1,ipady =40,ipadx=40)
key_5 = tk.Button(window,text="5",command=click_5).grid(row=4,column=2,ipady =40,ipadx=40)
key_6 = tk.Button(window,text="6",command=click_6).grid(row=4,column=3,ipady =40,ipadx=40)
key_7 = tk.Button(window,text="7",command=click_7).grid(row=5,column=1,ipady =40,ipadx=40)
key_8 = tk.Button(window,text="8",command=click_8).grid(row=5,column=2,ipady =40,ipadx=40)
key_9 = tk.Button(window,text="9",command=click_9).grid(row=5,column=3,ipady =40,ipadx=40)
key_0 = tk.Button(window,text="0",command=click_0).grid(row=6,column=2,ipady =40,ipadx=40)

key_decimal = tk.Button(window,text=",").grid(row=6,column=1,ipady =40,ipadx=40)
key_equals = tk.Button(window,text="=").grid(row=6,column=3,ipady =40,ipadx=40)

#FUNCTION PAD
key_add = tk.Button(window,text="+").grid(row=3,column=5,ipady =40,ipadx=40)
key_sub = tk.Button(window,text="-").grid(row=3,column=6,ipady =40,ipadx=40)
key_mul = tk.Button(window,text="*").grid(row=4,column=5,ipady =40,ipadx=40)
key_div = tk.Button(window,text="/").grid(row=4,column=6,ipady =40,ipadx=40)
key_pow = tk.Button(window,text="^").grid(row=5,column=5,ipady =40,ipadx=40)
key_roo = tk.Button(window,text="√").grid(row=5,column=6,ipady =40,ipadx=40)
key_mod = tk.Button(window,text="%").grid(row=6,column=5,ipady =40,ipadx=40)
key_fac = tk.Button(window,text="!").grid(row=6,column=6,ipady =40,ipadx=40)

#CALCPAD
key_delete = tk.Button(window,text="DELETE",command =click_delete).grid(row=8,column=1,ipady =20,ipadx=40)
key_clear = tk.Button(window,text="CLEAR",command =click_clear).grid(row=8,column=2,ipady =20,ipadx=40)
key_1_cache = tk.Button(window,text="CACHE").grid(row=8,column=3,ipady =20,ipadx=40)


window.mainloop()