import random as rd

"""
random_non_zero_int
input:max value (int), isPositive (boolean)
output:a non-zero int between 1 and max value that is positive if isPositive else the negative version is returned
"""

def random_non_zero_int(max:int,isPositive:bool)->int:
    if max <= 1:
        max = 1
    number_part = rd.randint(1,max)
    return number_part if isPositive else -1*number_part


"""
random_non_zero_int
input:max value (int), isPositive (boolean)
output: a single string that lists all the parameters in an application style word problem with their shared unit.
"""

def write_paramaters(parameters, unit):
    if len(parameters) == 1:
        return f"{parameters[0]} {unit}"
    else:
        holder = ""
        for i in range(len(parameters)):
            if i == len(parameters) - 1:
                holder += f"and {parameters[i]} {unit}"
            else:
                holder += f"{parameters[i]} {unit}, "
        return holder
            
def make_letter_choices(choices:list):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    holder = ""
    for i in range(len(choices)-1):
        holder += f"{alphabet[i]}. {choices[i]}, "
    return holder+f"{alphabet[len(choices)-1]}.{choices[-1]}"