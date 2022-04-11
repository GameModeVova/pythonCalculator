##
# @mainpage Python calculator VUT FIT IVS project
#
# @section description_main Description
# Calculator application developed in Python.
#
# @authors Vladimir Azarov (xazaro00)
# @authors Janos Laszlo Vasik (xvasik05)
# @authors Lucia Balazova (xbalaz18)
# @authors Nikolas Ospaly (xospal01)
#
# This program is licensed under the GNU General Public License v3.0.

##
# @file calc.py
# @brief Calculator source code developed in Python.
#
# @section desctription_calc Description
# Calculator software with a tkinter GUI, developed in Python.

# Imports
import math
import math_lib
import tkinter as tk
from tkinter import messagebox

def input_formating(user_input):
    """! Formats user input into a form suitable for the program.

    @param user_input       Input from user.

    @return                 Formatted input from user.
    """
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

def function_executioner(user_input):
    """! Executes currently entered operation.

    @param user_input       Input from user.

    @return                 Result from operation.
    """
    #ADDITION
    if user_input[-1] == "+":
        return(math_lib.add(user_input[0], user_input[1]))

    #SUBTRACTION
    if user_input[-1] == "-":
        return(math_lib.sub(user_input[0], user_input[1]))

    #MULTIPLICATION
    if user_input[-1] == "*":
        return(math_lib.mul(user_input[0], user_input[1]))

    #DIVISION
    if user_input[-1] == "/":
        return(math_lib.div(user_input[0], user_input[1]))

    #EXPONENT
    if user_input[-1] == "^":
        return(math_lib.exp(user_input[0], user_input[1]))

    #ROOT
    if user_input[-1] == "√":
        return(math_lib.root(float(user_input[0]), float(user_input[1])))

    #FACTORIAL
    if user_input[-1] == "!":
        return(math_lib.fact(user_input[0]))

    #REMAINDER
    if user_input[-1] == "%":
        return(math_lib.mod(user_input[0], user_input[1]))

def last_op(user_input):
    """! Returns true if the last character of the input is an operator.

    @param user_input       Input from user.

    @return                 True/False.
    """
    operators = "+.-*/^%√"
    if user_input[-1] in operators:
        return True
    else:
        return False


#Basic tkinter UI Layout
#---------------------------------------------------------------------------

#WINDOW CONFIG

## Main window of the graphical inteface.
window = tk.Tk()
window.title("Calculator")
window.iconbitmap("calc_icon.ico")
window.geometry("720x800")

#PLACEMENT GRID CONFIG
window.columnconfigure((0,4,7),weight=1)
window.columnconfigure((1,2,3,5,6),weight=3)

window.rowconfigure((0,2,7,9),weight=1)
window.rowconfigure((1,8), weight = 2)
window.rowconfigure((3,4,5,6), weight=3)

## Main menu.
head_menu = tk.Menu(window)

## Sub-menu with help options.
help_menu = tk.Menu(head_menu, tearoff=0)
help_menu.add_command(label="+",command=lambda:tk.messagebox.showinfo("Hint:+",
                                                                      "Calculates the sum of two numbers"))
help_menu.add_command(label="-",command=lambda:tk.messagebox.showinfo("Hint:-",
                                                                      "Subtracts the second number from the first one"))
help_menu.add_command(label="*",command=lambda:tk.messagebox.showinfo("Hint:*",
                                                                      "Multiplies the two numbers"))
help_menu.add_command(label="/",command=lambda:tk.messagebox.showinfo("Hint:/",
                                                                      "Calculates the quotient of the dividend and divisor"))
help_menu.add_command(label="^",command=lambda:tk.messagebox.showinfo("Hint:^",
                                                                      "Calculates the n-th power of the first number"))
help_menu.add_command(label="√",command=lambda:tk.messagebox.showinfo("Hint:√",
                                                                      "Calculates the n-th root of the second number"))
help_menu.add_command(label="!",command=lambda:tk.messagebox.showinfo("Hint:!",
                                                                      "Calculates the factorial"))
help_menu.add_command(label="%",command=lambda:tk.messagebox.showinfo("Hint:%",
                                                                      "Calculates the remainder of a division (modulo)"))
help_menu.add_command(label="Delete",command=lambda:tk.messagebox.showinfo("Hint: Delete",
                                                                      "Deletes the last character"))
help_menu.add_command(label="Cache",command=lambda:tk.messagebox.showinfo("Hint: Cache",
                                                                      "Returns the last solved number"))
help_menu.add_command(label="Clear",command=lambda:tk.messagebox.showinfo("Hint: Clear",
                                                                      "Clears all input"))
head_menu.add_cascade(label="Help", menu=help_menu)

window.config(menu=head_menu)

## List of color schemes.
default_set = ["#a5c663", "#354f00", "#7b9f35", "#d4ee9f"]
#0=button bg, 1=text, 2=window bg, 3=label bg

## Color of background in GUI.
window.configure(background=default_set[2])

#DISPLAY
# functions
# ---------------------------------------------------------------------------------------------------------------------------
## Current equation in cache.
current_val = ""
## Result of last operation.
l_res = ""
## Number of maximum characters in input/output.
char_limit = 30
## List of valid operators.
operators = ["+","*","/","%","^","!","√","-"]

def click_clear():
    """! Resets the calculator. (empties current values and operation)
    """
    global current_val
    global operation_c
    ## @var operation_c
    #   Boolean for catching douple operation
    current_val = ""
    operation_c = False
    d_num.set(current_val)

def click_delete():
    """! Deletes the last character from user input.
    """
    global current_val
    global operation_c

    if current_val[-1] in operators:
        operation_c = False
    current_val = current_val[0:-1]
    d_num.set(current_val)

# key entry
def click_1():
    """! Inputs a "1".
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    else:
        current_val = current_val + "1"
        d_num.set(current_val)

def click_2():
    """! Inputs a "2".
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    else:
        current_val = current_val + "2"
        d_num.set(current_val)

def click_3():
    """! Inputs a "3".
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    else:
        current_val = current_val + "3"
        d_num.set(current_val)

def click_4():
    """! Inputs a "4".
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    else:
        current_val = current_val + "4"
        d_num.set(current_val)

def click_5():
    """! Inputs a "5".
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    else:
        current_val = current_val + "5"
        d_num.set(current_val)

def click_6():
    """! Inputs a "6".
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    else:
        current_val = current_val + "6"
        d_num.set(current_val)

def click_7():
    """! Inputs a "7".
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    else:
        current_val = current_val + "7"
        d_num.set(current_val)


def click_8():
    """! Inputs a "8".
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    else:
        current_val = current_val + "8"
        d_num.set(current_val)

def click_9():
    """! Inputs a "9".
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    else:
        current_val = current_val + "9"
        d_num.set(current_val)


def click_0():
    """! Inputs a "0".
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    elif len(str(current_val))>=1 and [-1] == "/":
        tk.messagebox.showerror("Invalid operation", "Cannot divide by 0.")
    elif len(str(current_val)) >= 2 and current_val[-2] == "/" and current_val[-1] == "-":
        tk.messagebox.showerror("Invalid operation", "Cannot divide by 0.")
    else:
        current_val = current_val + "0"
        d_num.set(current_val)

def click_decimal():
    """! Inputs a decimal separator.
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    elif current_val == "":
        current_val = "0."
        d_num.set(current_val)
    elif last_op(current_val):
        tk.messagebox.showerror("Invalid input", "Floating point must follow a number.")
    else:
        current_val = current_val + "."
        d_num.set(current_val)


# label
# ---------------------------------------------------------------------------------------------------------------------------
## Current output shown to user in GUI.
d_num = tk.StringVar(window)
d_num.set(current_val)
## Text label of current output.
display = tk.Label(window,textvariable=d_num,font= 30)
display.grid(row=1,column=0,columnspan=7,ipady=20,ipadx=720)
display.configure(background=default_set[3], fg=default_set[1])

#NUMPAD
## Button for inputting a "1".
key_1 = tk.Button(window,text="1",command=click_1,bg=default_set[0],fg=default_set[1])\
    .grid(row=3,column=1,ipady =40,ipadx=40)
## Button for inputting a "2".
key_2 = tk.Button(window,text="2",command=click_2,bg=default_set[0],fg=default_set[1])\
    .grid(row=3,column=2,ipady =40,ipadx=40)
## Button for inputting a "3".
key_3 = tk.Button(window,text="3",command=click_3,bg=default_set[0],fg=default_set[1])\
    .grid(row=3,column=3,ipady =40,ipadx=40)
## Button for inputting a "4".
key_4 = tk.Button(window,text="4",command=click_4,bg=default_set[0],fg=default_set[1])\
    .grid(row=4,column=1,ipady =40,ipadx=40)
## Button for inputting a "5".
key_5 = tk.Button(window,text="5",command=click_5,bg=default_set[0],fg=default_set[1])\
    .grid(row=4,column=2,ipady =40,ipadx=40)
## Button for inputting a "6".
key_6 = tk.Button(window,text="6",command=click_6,bg=default_set[0],fg=default_set[1])\
    .grid(row=4,column=3,ipady =40,ipadx=40)
## Button for inputting a "7".
key_7 = tk.Button(window,text="7",command=click_7,bg=default_set[0],fg=default_set[1])\
    .grid(row=5,column=1,ipady =40,ipadx=40)
## Button for inputting a "8".
key_8 = tk.Button(window,text="8",command=click_8,bg=default_set[0],fg=default_set[1])\
    .grid(row=5,column=2,ipady =40,ipadx=40)
## Button for inputting a "9".
key_9 = tk.Button(window,text="9",command=click_9,bg=default_set[0],fg=default_set[1])\
    .grid(row=5,column=3,ipady =40,ipadx=40)
## Button for inputting a "0".
key_0 = tk.Button(window,text="0",command=click_0,bg=default_set[0],fg=default_set[1])\
    .grid(row=6,column=2,ipady =40,ipadx=40)
## Button for inputting a decimal separator.
key_decimal = tk.Button(window,text=",",command=click_decimal,bg=default_set[0],fg=default_set[1])\
    .grid(row=6,column=1,ipady =40,ipadx=40)

#FUNCTION PAD
operation_c = False
def double_input():
    """! Checks for double input. If it is caught, it calculates the first equation.
    """
    global operation_c
    global current_val

    for char in current_val:
        if char in operators:
            operation_c = True

    if operation_c == True:
        equals()
        current_val=l_res
        d_num.set(current_val)
    else:
        operation_c = True

def click_add():
    """! Inputs a "+", to calculate addition.
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    elif str(current_val) == "":
        current_val = "0+"
        d_num.set(current_val)
    elif last_op(current_val):
        tk.messagebox.showerror("Invalid input", "Addition must follow a number")
    else:
        double_input()
        current_val = current_val + "+"
        d_num.set(current_val)

def click_sub():
    """! Inputs a "-", to calculate subtraction.
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    elif str(current_val) == "":
        current_val = current_val + "-"
        d_num.set(current_val)
    elif current_val[-1] == "-":
        click_delete()
        click_add()
    else:
        double_input()
        current_val = current_val + "-"
        d_num.set(current_val)

def click_mul():
    """! Inputs a "*", to calculate multiplication.
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    elif str(current_val) == "":
        current_val = "0*"
        d_num.set(current_val)
    elif last_op(current_val):
        tk.messagebox.showerror("Invalid input", "Multiplication must follow a number")
    else:
        double_input()
        current_val = current_val + "*"
        d_num.set(current_val)

def click_div():
    """! Inputs a "/", to calculate division.
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    elif str(current_val) == "":
        current_val = "0/"
        d_num.set(current_val)
    elif last_op(current_val):
        tk.messagebox.showerror("Invalid input", "Division must follow a number")
    else:
        double_input()
        current_val = current_val + "/"
        d_num.set(current_val)

def click_pow():
    """! Inputs a "^", to calculate n-th power.
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    elif str(current_val) == "":
        current_val = "0^"
        d_num.set(current_val)
    elif last_op(current_val):
        tk.messagebox.showerror("Invalid input", "This operator must follow a number")
    else:
        double_input()
        current_val = current_val + "^"
        d_num.set(current_val)

def click_roo():
    """! Inputs a "√", to calculate root.
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    elif str(current_val)  == "":
        current_val = "2√"
        d_num.set(current_val)
    elif last_op(current_val):
        tk.messagebox.showerror("Invalid input", "This operator must follow a number")
    else:
        double_input()
        current_val = current_val + "√"
        d_num.set(current_val)

def click_mod():
    """! Inputs a "%", to calculate modulo.
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    elif str(current_val)  == "":
        current_val = "0%"
        d_num.set(current_val)
    elif last_op(current_val):
        tk.messagebox.showerror("Invalid input", "Modulo must follow a number")
    else:
        double_input()
        current_val = current_val + "%"
        d_num.set(current_val)

def click_fac():
    """! Inputs a "!", to calculate factorial.
    """
    global current_val
    if len(str(current_val))>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")
    elif str(current_val) == "":
        current_val = "0!"
        d_num.set(current_val)
    elif last_op(current_val) or current_val[-1] == "!":
        tk.messagebox.showerror("Invalid input", "Factorial must follow a number")
    else:
        double_input()
        current_val = current_val + "!"
        d_num.set(current_val)
#-------------------------------------------------------------------------------------------------------------------------
## Button for calculating addition.
key_add = tk.Button(window,text="+",command =click_add,bg=default_set[0],fg=default_set[1])\
    .grid(row=3,column=5,ipady =40,ipadx=40)
## Button for calculating subtraction.
key_sub = tk.Button(window,text="-",command =click_sub,bg=default_set[0],fg=default_set[1])\
    .grid(row=3,column=6,ipady =40,ipadx=40)
## Button for calculating multiplication.
key_mul = tk.Button(window,text="*",command =click_mul,bg=default_set[0],fg=default_set[1])\
    .grid(row=4,column=5,ipady =40,ipadx=40)
## Button for calculating division.
key_div = tk.Button(window,text="/",command =click_div,bg=default_set[0],fg=default_set[1])\
    .grid(row=4,column=6,ipady =40,ipadx=40)
## Button for calculating n-th power.
key_pow = tk.Button(window,text="^",command =click_pow,bg=default_set[0],fg=default_set[1])\
    .grid(row=5,column=5,ipady =40,ipadx=40)
## Button for calculating n-th root.
key_roo = tk.Button(window,text="√",command =click_roo,bg=default_set[0],fg=default_set[1])\
    .grid(row=5,column=6,ipady =40,ipadx=40)
## Button for calculating modulo.
key_mod = tk.Button(window,text="%",command =click_mod,bg=default_set[0],fg=default_set[1])\
    .grid(row=6,column=5,ipady =40,ipadx=40)
## Button for calculating factorial.
key_fac = tk.Button(window,text="!",command =click_fac,bg=default_set[0],fg=default_set[1])\
    .grid(row=6,column=6,ipady =40,ipadx=40)

#CALCPAD
## Button for deleting the last character.
key_delete = tk.Button(window,text="DELETE",command =click_delete,bg=default_set[0],fg=default_set[1])\
    .grid(row=8,column=1,ipady =20,ipadx=40)
## Button for clearing all user input.
key_clear = tk.Button(window,text="CLEAR",command =click_clear,bg=default_set[0],fg=default_set[1])\
    .grid(row=8,column=2,ipady =20,ipadx=40)

#INPUT TRANSFORMATION
## Result of current equation.
solution = current_val

def equals():
    """! Calculates the result of the input equation, and prints it out in the GUI.
    """
    global solution
    global l_res
    global current_val
    global operation_c
    global operators

    if len(str(current_val)) >= 0:
        if str(current_val)[-1] in operators and str(current_val)[-1] != "!":
            tk.messagebox.showerror("Input error", "Invalid input format")
            return

    solution = str(function_executioner(input_formating(current_val)))
    if solution[-1] == "0" and solution[-2] == ".":
        solution=solution[0:-2]

    l_res = solution
    d_num.set(solution)
    operation_c = False
    current_val = solution

def show_cache():
    """! Deletes the current input and replaces it with last result.
    """
    global l_res
    global current_val
    current_val=l_res
    d_num.set(current_val)

## Button for calculating and showing result.
key_equals = tk.Button(window,text="=",command=equals,bg=default_set[0],fg=default_set[1])\
    .grid(row=6,column=3,ipady =40,ipadx=40)
## Button for showing last result.
key_1_cache = tk.Button(window,text="CACHE",command=show_cache, bg=default_set[0],fg=default_set[1])\
    .grid(row=8,column=3,ipady =20,ipadx=40)


#KEBINDS
#------------------------------------------------------------------------------------------------------------------------
window.bind("0",lambda x:click_0())
window.bind("1",lambda x:click_1())
window.bind("2",lambda x:click_2())
window.bind("3",lambda x:click_3())
window.bind("4",lambda x:click_4())
window.bind("5",lambda x:click_5())
window.bind("6",lambda x:click_6())
window.bind("7",lambda x:click_7())
window.bind("8",lambda x:click_8())
window.bind("9",lambda x:click_9())

window.bind("+",lambda x:click_add())
window.bind("-",lambda x:click_sub())
window.bind("*",lambda x:click_mul())
window.bind("/",lambda x:click_div())
window.bind("^",lambda x:click_pow())
window.bind("!",lambda x:click_fac())
window.bind("%",lambda x:click_mod())

window.bind("<BackSpace>",lambda x:click_delete())
window.bind("c",lambda x:click_clear())
window.bind("l",lambda x:show_cache())

window.mainloop()

### End of file math_lib.py ###