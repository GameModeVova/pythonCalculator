import math
import math_lib
import tkinter as tk
from tkinter import messagebox

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

#ADDING ALL FUNCTIONS FOR A RESULT, ALSO SAVES RESULT INTO CASHE
def solver(user_input):
    return(function_executioner(input_formating(error_checker(user_input))))

#RETURNS TRUE IF LAST CHARACTER OF THE INPUT IS AN OPERATOR
def last_op(user_input):
    operators = "+.-*/^%√"
    if user_input[-1] in operators:
        return True
    else:
        return False


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
head_menu.add_cascade(label="Help", menu=help_menu)

window.config(menu=head_menu)

#colour schemes
default_set = ["#a5c663", "#354f00", "#7b9f35", "#d4ee9f"]
#0=button bg, 1=text, 2=window bg, 3=label bg

window.configure(background=default_set[2])

#DISPLAY
# functions
# ---------------------------------------------------------------------------------------------------------------------------
current_val = ""
l_res = ""
char_limit = 30

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
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    current_val = current_val + "1"
    d_num.set(current_val)

def click_2():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    current_val = current_val + "2"
    d_num.set(current_val)

def click_3():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    current_val = current_val + "3"
    d_num.set(current_val)

def click_4():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    current_val = current_val + "4"
    d_num.set(current_val)

def click_5():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    current_val = current_val + "5"
    d_num.set(current_val)

def click_6():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    current_val = current_val + "6"
    d_num.set(current_val)

def click_7():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    current_val = current_val + "7"
    d_num.set(current_val)


def click_8():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    current_val = current_val + "8"
    d_num.set(current_val)

def click_9():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    current_val = current_val + "9"
    d_num.set(current_val)


def click_0():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    if current_val[-1] == "/":
        tk.messagebox.showerror("Invalid operation", "Cannot divide by 0.")
    elif len(current_val) >= 2 and current_val[-2] == "/" and current_val[-1] == "-":
        tk.messagebox.showerror("Invalid operation", "Cannot divide by 0.")
    else:
        current_val = current_val + "0"
        d_num.set(current_val)

def click_decimal():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    if current_val == "":
        current_val = "0."
        d_num.set(current_val)
    elif last_op(current_val):
        tk.messagebox.showerror("Invalid input", "Floating point must follow a number.")
    else:
        current_val = current_val + "."
        d_num.set(current_val)


# label
# ---------------------------------------------------------------------------------------------------------------------------
d_num = tk.StringVar(window)
d_num.set(current_val)
display = tk.Label(window,textvariable=d_num,font= 30)
display.grid(row=1,column=0,columnspan=7,ipady=20,ipadx=720)
display.configure(background=default_set[3], fg=default_set[1])

#NUMPAD
key_1 = tk.Button(window,text="1",command=click_1,bg=default_set[0],fg=default_set[1])\
    .grid(row=3,column=1,ipady =40,ipadx=40)
key_2 = tk.Button(window,text="2",command=click_2,bg=default_set[0],fg=default_set[1])\
    .grid(row=3,column=2,ipady =40,ipadx=40)
key_3 = tk.Button(window,text="3",command=click_3,bg=default_set[0],fg=default_set[1])\
    .grid(row=3,column=3,ipady =40,ipadx=40)
key_4 = tk.Button(window,text="4",command=click_4,bg=default_set[0],fg=default_set[1])\
    .grid(row=4,column=1,ipady =40,ipadx=40)
key_5 = tk.Button(window,text="5",command=click_5,bg=default_set[0],fg=default_set[1])\
    .grid(row=4,column=2,ipady =40,ipadx=40)
key_6 = tk.Button(window,text="6",command=click_6,bg=default_set[0],fg=default_set[1])\
    .grid(row=4,column=3,ipady =40,ipadx=40)
key_7 = tk.Button(window,text="7",command=click_7,bg=default_set[0],fg=default_set[1])\
    .grid(row=5,column=1,ipady =40,ipadx=40)
key_8 = tk.Button(window,text="8",command=click_8,bg=default_set[0],fg=default_set[1])\
    .grid(row=5,column=2,ipady =40,ipadx=40)
key_9 = tk.Button(window,text="9",command=click_9,bg=default_set[0],fg=default_set[1])\
    .grid(row=5,column=3,ipady =40,ipadx=40)
key_0 = tk.Button(window,text="0",command=click_0,bg=default_set[0],fg=default_set[1])\
    .grid(row=6,column=2,ipady =40,ipadx=40)

key_decimal = tk.Button(window,text=",",command=click_decimal,bg=default_set[0],fg=default_set[1])\
    .grid(row=6,column=1,ipady =40,ipadx=40)

#FUNCTION PAD

def click_add():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    if current_val == "":
        current_val = "0+"
        d_num.set(current_val)
    elif last_op(current_val):
        tk.messagebox.showerror("Invalid input", "Addition must follow a number")
    else:
        current_val = current_val + "+"
        d_num.set(current_val)

def click_sub():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    if current_val == "":
        current_val = current_val + "-"
        d_num.set(current_val)
    elif current_val[-1] == "-":
        click_delete()
        click_add()
    else:
        current_val = current_val + "-"
        d_num.set(current_val)


def click_mul():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    if current_val == "":
        current_val = "0*"
        d_num.set(current_val)
    elif last_op(current_val):
        tk.messagebox.showerror("Invalid input", "Multiplication must follow a number")
    else:
        current_val = current_val + "*"
        d_num.set(current_val)

def click_div():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    if current_val == "":
        current_val = "0/"
        d_num.set(current_val)
    elif last_op(current_val):
        tk.messagebox.showerror("Invalid input", "Division must follow a number")
    else:
        current_val = current_val + "/"
        d_num.set(current_val)

def click_pow():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    if current_val == "":
        current_val = "0^"
        d_num.set(current_val)
    elif last_op(current_val):
        tk.messagebox.showerror("Invalid input", "This operator must follow a number")
    else:
        current_val = current_val + "^"
        d_num.set(current_val)

def click_roo():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    if current_val == "":
        current_val = "2√"
        d_num.set(current_val)
    elif last_op(current_val):
        tk.messagebox.showerror("Invalid input", "This operator must follow a number")
    else:
        current_val = current_val + "√"
        d_num.set(current_val)

def click_mod():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    if current_val == "":
        current_val = "0%"
        d_num.set(current_val)
    elif last_op(current_val):
        tk.messagebox.showerror("Invalid input", "Modulo must follow a number")
    else:
        current_val = current_val + "%"
        d_num.set(current_val)

def click_fac():
    global current_val
    if len(current_val)>= char_limit:
        tk.messagebox.showerror("Error", "Input lenght reached.")

    if current_val == "":
        current_val = "0!"
        d_num.set(current_val)
    elif last_op(current_val) or current_val[-1] == "!":
        tk.messagebox.showerror("Invalid input", "Factorial must follow a number")
    else:
        current_val = current_val + "!"
        d_num.set(current_val)
#-------------------------------------------------------------------------------------------------------------------------
key_add = tk.Button(window,text="+",command =click_add,bg=default_set[0],fg=default_set[1])\
    .grid(row=3,column=5,ipady =40,ipadx=40)
key_sub = tk.Button(window,text="-",command =click_sub,bg=default_set[0],fg=default_set[1])\
    .grid(row=3,column=6,ipady =40,ipadx=40)
key_mul = tk.Button(window,text="*",command =click_mul,bg=default_set[0],fg=default_set[1])\
    .grid(row=4,column=5,ipady =40,ipadx=40)
key_div = tk.Button(window,text="/",command =click_div,bg=default_set[0],fg=default_set[1])\
    .grid(row=4,column=6,ipady =40,ipadx=40)
key_pow = tk.Button(window,text="^",command =click_pow,bg=default_set[0],fg=default_set[1])\
    .grid(row=5,column=5,ipady =40,ipadx=40)
key_roo = tk.Button(window,text="√",command =click_roo,bg=default_set[0],fg=default_set[1])\
    .grid(row=5,column=6,ipady =40,ipadx=40)
key_mod = tk.Button(window,text="%",command =click_mod,bg=default_set[0],fg=default_set[1])\
    .grid(row=6,column=5,ipady =40,ipadx=40)
key_fac = tk.Button(window,text="!",command =click_fac,bg=default_set[0],fg=default_set[1])\
    .grid(row=6,column=6,ipady =40,ipadx=40)

#CALCPAD
key_delete = tk.Button(window,text="DELETE",command =click_delete,bg=default_set[0],fg=default_set[1])\
    .grid(row=8,column=1,ipady =20,ipadx=40)
key_clear = tk.Button(window,text="CLEAR",command =click_clear,bg=default_set[0],fg=default_set[1])\
    .grid(row=8,column=2,ipady =20,ipadx=40)

#INPUT TRANSFORMATION
solution = current_val

def equals():
    global solution
    global l_res
    global current_val
    solution = solver(current_val)
    l_res = solution
    d_num.set(solution)
    current_val = ""

def show_cache():
    global l_res
    global current_val
    current_val=l_res
    d_num.set(current_val)


key_equals = tk.Button(window,text="=",command=equals,bg=default_set[0],fg=default_set[1])\
    .grid(row=6,column=3,ipady =40,ipadx=40)

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