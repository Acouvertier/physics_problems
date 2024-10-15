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

def oneRateProblem():
    ans = rd.randint(2,10)
    nice_factors = [1,2,4,5,8,10,16,20,25,40,50]
    
    units = {
        "length": ["meters", "feet", "inches", "yards", "miles"],
        "time": ["seconds", "hours", "minutes", "years", "days"],
        "mass": ["pounds", "kilograms", "grams", "gallons", "cups"]
                }
    
    rate = Fraction(rd.choice(nice_factors),rd.choice(nice_factors))
        
    given = (ans*(rate.denominator)/(rate.numerator))
    
    [givenUnits, ansUnits, missingUnits] = rd.sample(list(units.keys()),3)

    gu = rd.choice(units[givenUnits])
    au = rd.choice(units[ansUnits])
    mu = rd.choice(units[missingUnits])

    if set([givenUnits,ansUnits]) == set(["length","mass"]):
        if givenUnits == "length":
            wordproblemsLM = [
                f"A certain cement truck has covered a distance of {given} {gu} while laying cement.\nIf the truck can lay {rate.numerator} {au} of cement for every {rate.denominator} {gu}, how many {au} of cement have been layed?",
                f"While driving cross country, the odometer has increased by {given} {gu}.\nIf your car is known to use {rate.numerator} {au} of gas for every {rate.denominator} {gu} traveled, how many {au} of gas have been used?",
                f"The local fair is hosting a hot-dog eating contest where a meter goes up {rate.denominator} {gu} for every {rate.numerator} {au} of hot dogs eaten.\nIf the meter is up {given} {gu}, how many {au} of hot dogs have been eaten?"
                ]
            question = rd.choice(wordproblemsLM)
        else:
            wordproblemsML = [
                f"When drawing lines on the road, machines keep a constant pace of {rate.numerator} {au} of road covered using exactly {rate.denominator} {gu} of paint. In one day, {given} {gu} of paint is actually used. What is the length of road covered?",
                f"A certain metalmaker can craft {given} {gu} of metal during their shift. If one sheet of metal is {rate.numerator} {au} for every {rate.denominator} {gu} of metal used, what is the total length of sheet produced?",
                f"At the fair, a contestant has eaten {given} {gu} of ice cream. Behind them a gauge goes up based on how much ice cream they eat. If {rate.denominator} {gu} of ice cream causes the gauge to rise {rate.numerator} {au}, how tall is the gauge behind the contestant?"
                ]
            question = rd.choice(wordproblemsML)
    
    if set([givenUnits,ansUnits]) == set(["length","time"]):
        if givenUnits == "length":
            wordproblemsLT = [
                f"A car has traveled {given} {gu}. Based on the Kelly Blue Book, it can travel consistently for {rate.denominator} {gu} every {rate.numerator} {au}. How much time has passed since the car got on the road?",
                f"Bored on a weekend, you watch a snail travel {given} {gu} on the sidewalk. Going inside, you learn it takes snails {rate.numerator} {au} to travel {rate.denominator} {gu}. How much time passed while watching the snail?"
            ]
            question = rd.choice(wordproblemsLT)
        else:
            wordproblemsTL = [
                f"Between stops, trains reach a speed of {rate.numerator} {au} every {rate.denominator} {gu}. If the conductor says you have {given} {gu} before arrving at your stop, what is the distance between the stop?",
                f"In a recent study, scientists discovered hair can grow {rate.numerator} {au} every {rate.denominator} {gu} in some cases. To test this you decide to grow your hair out for {given} {gu}. If the scientists are correct, how much extra hair should you have?"
            ]
            question = rd.choice(wordproblemsTL)
    if set([givenUnits,ansUnits]) == set(["time","mass"]):
        if givenUnits == "time":
            wordproblemsTM = [
                f"A typical shift for an ice cream truck is {given} {gu}. The machine in the truck dispenses ice cream at a constant rate to keep costs low. To be precise, the machine dispenses {rate.numerator} {au} of ice cream every {rate.denominator} {gu}. How many {au} of ice cream are dispensed in a regular shift?",
                f"Popcorn at the movie theatre is made at constant rate: {rate.denominator} {gu} to make {rate.numerator} {au} of popcorn. If the machine runs for {given} {gu}, how many {au} of popcorn is made?"
            ]
            question =  rd.choice(wordproblemsTM)
        else:
            wordproblemsMT = [
                f"While sitting in traffic, your car has used {given} {gu} of gas. The standard idling rate is known to be {rate.numerator} {au} of run time for every {rate.denominator} {gu} of gas used. How long has your car been idling for?",
                f"Wind turbines are incredibly efficient at moving vast quantities of air. In lab testing, scientists can create turbines that move {rate.denominator} {gu} of air every {rate.numerator} {au}. In the air, these turbines typically move {given} {gu} of air in a single trip. How much time does it take to complete a single trip?"
            ]
            question = rd.choice(wordproblemsMT)
    
    return question + f" ANSWER: {ans} {au}"

print(sv_absolute_value("w","standard"))