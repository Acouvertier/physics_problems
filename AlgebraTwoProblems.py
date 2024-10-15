import random as rd
import numpy as np
import sympy as sp
from sympy import I
from Helpers import random_non_zero_int

"""
make_quadratic
inputs: var_str (string for the variable), num_real_sol (number of desired real solutions)
output: a Sympy Expression for the quadratic with randomly defined solutions. (and the symbol used as variable)
"""

def make_quadratic(var_str:str, num_real_sol:int):
    if num_real_sol not in set([0,1,2]):
        print("Quadratic has an upperbound of 2 solutions and lowerbound of 0, setting to 2")
        num_real_sol = 2
    
    a = random_non_zero_int(3,rd.choice([True,False]))
    x = sp.symbols(var_str)
    if num_real_sol == 0:
        re_part = rd.randint(-10,10)
        if rd.choice([True,False]):
            im_part = random_non_zero_int(5,True)
        else: 
            im_part = random_non_zero_int(3,True) * sp.sqrt(random_non_zero_int(20,True))
        
        function = sp.expand(a*(x - re_part + I*im_part)*(x - re_part - I*im_part))
    
    elif num_real_sol == 1:
        single_sol = sp.Rational(random_non_zero_int(10,rd.choice([True,False])),random_non_zero_int(4,True))
        function = sp.expand(a*(x-single_sol)**2)
    
    else: 
        sols1 = random_non_zero_int(8,rd.choice([True,False]))
        sols2 = sols1 + rd.choice([sp.Rational(random_non_zero_int(8,rd.choice([True,False])),random_non_zero_int(4,True)),random_non_zero_int(8,rd.choice([True,False]))])
        function = sp.expand(a*(x-sols1)*(x-sols2))

    return [function,x]

"""
all_quadratic_features
inputs: var_str (string for variable)
output: a Sympy Expression for the quadratic and a dict of features

features (dict):
KEYS

x_ints:
y_int:
AoS:
vertex:
extrema:
inc:
dec:
range:
abc:


"""
def all_quadratic_features(var_str:str):

    [my_quadratic,x] = make_quadratic(var_str, rd.choice([0,1,2]))
    
    x_ints = sp.solve(my_quadratic,x)
    y_int = my_quadratic.subs(x,0)
    AoS = sum(x_ints)/2 if len(x_ints) == 2 else x_ints[0]
    vertex = (AoS, my_quadratic.subs(x,AoS))
    extrema = (y_int > vertex[1]) #True is "min"
    inc = f"(-oo,{AoS})"
    dec = f"({AoS},oo)"
    y_range = f"(-oo,{vertex[1]}]"
    if extrema: 
        inc, dec = dec, inc
        y_range = f"[{vertex[1]},oo)"
    
    return [
        my_quadratic,
        x,
        {
            "x_int":x_ints,
            "y_int":y_int,
            "AoS":AoS,
            "vertex":vertex,
            "extrema": "min" if extrema else "max",
            "inc": inc,
            "dec": dec,
            "range": y_range,
            "abc": (sp.Rational((y_int-(vertex[1])),(vertex[0])**2),sp.Rational(-2*((y_int-(vertex[1]))),(vertex[0])),y_int)
        }
    ]

"""
discriminant_check
input: var_str (string representation of the variable)
output: list contains -->
my_quadratic -> randomly generated Sympy Expression for the quadratic used
x -> Sympy Symbol used in my_quadratic
disc -> value of the discriminant
num_sols -> number real solutions based on the rules of the discriminant
"""

def discriminant_check(var_str:str):
    
    [my_quadratic, x, feature_dict] = all_quadratic_features(var_str)

    (a,b,c) = feature_dict["abc"]
    disc = b**2 - 4*a*c
    
    if disc < 0: 
        num_sols = 0
    elif disc == 0:
        num_sols = 1
    else: num_sols = 2

    return[my_quadratic,x,disc,num_sols]

