import random as rd
import numpy as np
import sympy as sp #allows for symbolic math
from Helpers import random_non_zero_int
from fractions import Fraction

"""
Concept: Solving Single Variable Equations

problem_type:
"ims" -> infinite solutions (0=0)
"none" -> no solutions (A=0, A!=0)
"unqiue" -> one solution

random number of terms
"""

def sv_equation(var_str:str, problem_type:str) -> list[str]:
    
    pt = problem_type.lower()
    if pt not in set(["none","unique","ims"]): 
        print("invalid solution choice.")
        return None
    
    x = sp.symbols(var_str)
    #default is none
    a_total = 0
    b_total = random_non_zero_int(20,rd.choice([True,False]))
    solution = "none"

    if pt == "unique":
        a_total = random_non_zero_int(4,rd.choice([True,False]))
        if rd.choice([True,False]):
            b_total = random_non_zero_int(5,rd.choice([True,False])) * a_total
        solution = str(sp.Rational(b_total,a_total))
    elif pt == 'ims':
        b_total = 0
        solution = 'ims'

    num_coeffs = rd.randint(2,6)
    num_consts = rd.randint(2,6)

    current_coeffs = [random_non_zero_int(5,rd.choice([True,False])) for _ in range(num_coeffs-1)]
    current_consts = [random_non_zero_int(5,rd.choice([True,False])) for _ in range(num_consts-1)]
    
    last_coeff = a_total - sum(current_coeffs)
    last_const = b_total - sum(current_consts)

    current_coeffs.append(last_coeff)
    current_consts.append(last_const)

    lhs_coeffs, rhs_coeffs = current_coeffs[0:sp.floor(num_coeffs/2)], current_coeffs[sp.floor(num_coeffs/2):]
    lhs_const, rhs_const = current_consts[0:sp.floor(num_consts/2)], current_consts[sp.floor(num_consts/2):]
    
    lhs = 0
    for elt in lhs_coeffs:
        lhs += sp.UnevaluatedExpr(elt*x)
    for elt in lhs_const:
        lhs += sp.UnevaluatedExpr(-elt)

    rhs = 0
    for elt in rhs_coeffs:
        rhs += sp.UnevaluatedExpr(-elt*x)
    for elt in rhs_const:
        rhs += sp.UnevaluatedExpr(elt)

    return [f"{lhs} = {rhs}", solution]

"""
Concept: Solving Single Variable Absolute Values

Inputs:
var_str: a string representation of the single variable
problem_type: a string representation of the absolute value problem type
"standard" -> a|bx+c|+d = e
"outside" -> a|bx+c|+d = ex + f
"double" -> |bx+c| = |ex + f|
where x is the variable
"""

def sv_absolute_value(var_str:str, problem_type:str):

    pt = problem_type.lower()
    if pt not in set(["standard","outside","double"]): 
        print("invalid solution choice.")
        return None
    
    x = sp.symbols(var_str,real=True)

    if pt == "standard":
        a = random_non_zero_int(5,rd.choice([True,False]))
        
        e_minus_d = random_non_zero_int(5,rd.choice([True,False]))*a
        d = rd.randint(-5,5)
        e =  e_minus_d + d
        
        lhs = a * sp.Abs(random_non_zero_int(10,rd.choice([True,False]))*x+rd.randint(-10,10)) + d
        rhs = e
        
        solution = sp.solve(lhs-rhs,x)

    elif pt == "outside":
        [a,b,c,d,e,f] = [random_non_zero_int(10,rd.choice([True,False])) for _ in range(6)]
        
        lhs = a * sp.Abs(b*x+c) + d
        rhs = e * x + f
        
        solution = sp.solve(lhs-rhs,x)

    else:
        [b,c,e,f] = [random_non_zero_int(1,10,rd.choice([True,False])) for _ in range(4)]
        
        lhs = sp.Abs(b*x+c)
        rhs = sp.Abs(e*x+f)
        
        solution = sp.solve(lhs-rhs,x)
    
    return [f"{lhs} = {rhs}",solution]


"""
input: problem_type:int
1 -> average
2 -> final = initial + change
3 -> absolute deviation
4 -> sum of parts = whole
"""
def sv_word_problem(problem_type:int):
    x = sp.symbols("x",real=True)
    
    if problem_type == 1: #average word problem
        given_data = rd.choices(range(1,50),k=rd.randint(3,7))
        known_mean = np.mean(given_data)
        ans = given_data.pop(rd.choice(range(len(given_data))))
        given_data.append(x)
        rd.shuffle(given_data)
        return f"Create a real-world word problem where the average of a set of numbers is {known_mean}, and one number, {x}, in the set is missing. The problem should require solving for the missing number using the average equation. The full list is {given_data} and the correct answer is {ans}. The problem should involve practical scenarios that an Algebra 1 student would encounter."
    
    elif problem_type == 2: #constant rate of change
        rate = Fraction(random_non_zero_int(15,True),random_non_zero_int(5,rd.choice([True,False]))).limit_denominator()
        ans = random_non_zero_int(15,True)
        final = random_non_zero_int(30,rd.choice([True,False]))
        initial = final - rate*ans
        return f"Create a real-world word problem where the relationship follows the equation final = initial + rate * value. The problem should ask to solve for either the final, initial, or value, based on the provided information. The correct values are: final = {final}, initial = {initial}, rate = {rate}, and value = {ans}. The problem should involve practical scenarios that an Algebra 1 student would encounter."
    
    elif problem_type == 3:
        center = rd.randint(-100,100)
        deviations = random_non_zero_int(10,True)
        inequality_dict = {
            "less than": "<=",
            "greater than": ">=",
            "equal to": "==",
            "at least": ">=",
            "at most": "<+" 
        }
        relative = rd.choice(list(inequality_dict.keys()))

        ans = sp.reduce_abs_inequality(sp.Abs(x-center) - deviations, inequality_dict[relative], x)
        return f"Create a word problem that tests the concept of absolute deviation. The problem should provide a central value of {center} and an allowed absolute deviation of {deviations}. The student should be asked for the values about the center that are {relative} to the provided deviation. The answer, which is {ans}, should be expressed as an inequality or in set notation, depending on the instruction. The problem should involve a practical scenario."
    
    elif problem_type  == 4:
        parts = rd.choices(range(1,50),k=rd.randint(3,7))
        total = sum(parts)
        ans = parts.pop(rd.choice(range(len(parts))))
        return f"Create a real-world word problem where several parts of a whole are known, but one part is missing. The problem should require solving for the missing part when the sum of all the parts (the whole) is provided. The known parts are given as the list: {parts}, and the total (whole) is provided as a single number, {total}. The problem should involve a practical scenario that an Algebra 1 student would encounter. The problem should ask the student to solve for the missing part, the answer is {ans}."

    


