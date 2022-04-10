#profile using cprofile

import math_lib
import sys 
import re

def calc_arithm_mean(data):
    sum_of_all = 0
    for num in data: 
        sum_of_all = math_lib.add(num, sum_of_all)
    arithm_mean = math_lib.div(1, sum_of_all)
    return arithm_mean


def calc_std_dev(arithm_mean, data):
    sum = 0 
    N = len(data)
    arithm_mean_squared = math_lib.exp(arithm_mean, 2)

    for num in data:
        num_squared = math_lib.exp(num, 2)
        arithm_mean_squared_multiplied_by_len = math_lib.mul(N, arithm_mean_squared)
        interm = math_lib.sub(num_squared, arithm_mean_squared_multiplied_by_len)
        sum = math_lib.add(interm, sum)

    len_minus_one = math_lib.sub(N, 1)
    one_div_by_len_minus_one = math_lib.div(1, len_minus_one)
    multiplied = math_lib.mul(one_div_by_len_minus_one, sum)
    std_dev = math_lib.root(multiplied,2)
    return std_dev 

def main():
    data = ""

    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        data+=line

    data = (re.sub(r"\W+", " ", data)).split(" ")

    while (" " in data):
        data.remove(" ")
    while ("" in data):
        data.remove("")
    am = calc_arithm_mean(data)
    print(calc_std_dev(am, data))

main()    



