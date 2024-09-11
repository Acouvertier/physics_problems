import random as rd
import numpy as np
import math
import statistics

class MathProblems:

    def __init__(self):
        pass
    
    """Algebra 1"""
    def plusOrMinus(value):
        return f"+ {value}" if abs(value) == value else f"- {abs(value)}"
    
    def correctCoeff(value,leading=False):
        if abs(value) == 1:
            if leading:
                front = ""
            else:
                front = "+ "
            
            return front if value > 0 else "-"
        else:
            if abs(value) == value: 
                sign = "+"
            else:
                sign = "-"
            
            if leading:
                front = value 
            else: 
                front = f"{sign} {abs(value)}"
            
            return front
        
        

        
    def setGenericCoefficients(hasOneSolution=True):
        if hasOneSolution:
            [coeff1,ans] = [rd.choice([_ for _ in range(-10,10) if _ != 0]),rd.randint(-10,10)]
            coeff2 = -coeff1*ans

        else:
            coeff1 = 0
            coeff2 = rd.choice([0,rd.randint(-10,10)])
            if coeff2 == 0:
                ans = "IMS"
            else:
                ans = "No Solutions"
        return [coeff1, coeff2, ans]

    def oneSidedSingleVariable(varName: str):
        [a1, coeff2, ans] = MathProblems.setGenericCoefficients()
        
        a2 = rd.randint(-10,10)
        a3 = a2 - coeff2
        return f"{MathProblems.correctCoeff(a1)}{varName} {MathProblems.plusOrMinus(a2)} = {a3} ; {varName} = {ans}"
    
    def twoSidedSingleVariable(varName: str, form=1 ,hasOneSolution=True):
        [coeff1, coeff2, ans] = MathProblems.setGenericCoefficients(hasOneSolution)
        if form == 1:
            a2 = rd.randint(-10,10)
            a4 = a2 - coeff2

            a1 = rd.randint(-10,10)
            a3 = a1 - coeff1

            return f"{MathProblems.correctCoeff(a1,True)}{varName} {MathProblems.plusOrMinus(a2)} = {MathProblems.correctCoeff(a3,True)}{varName} {MathProblems.plusOrMinus(a4)} ; {varName} = {ans}"
        
        elif form == 2:
            [a4, a6] = [rd.randint(-10,10) for _ in range(2)]
            a2 = coeff2 + np.sum([a4, a6])

            [a1, a3] = [rd.randint(-10,10) for _ in range(2)]
            a5 = np.sum([a1, a3]) - coeff1

            return f"{MathProblems.correctCoeff(a1,True)}{varName} {MathProblems.plusOrMinus(a2)} {MathProblems.correctCoeff(a3)}{varName} = {a4} {MathProblems.correctCoeff(a5)}{varName} {MathProblems.plusOrMinus(a6)} ; {varName} = {ans}"
        
        elif form == 3: 
            [a1, a2] = [rd.randint(-10,10) for _ in range(2)]
            a4 = np.sum([a1, a2]) - coeff1

            
            [a3, a5] = [rd.randint(-10,10) for _ in range(2)]
            a6 = a2*a3 - a4*a5 - coeff2

            return f"{MathProblems.correctCoeff(a1,True)}{varName} {MathProblems.correctCoeff(a2)}({varName} {MathProblems.plusOrMinus(a3)}) = {MathProblems.correctCoeff(a4,True)}({varName} {MathProblems.plusOrMinus(a5)}) {MathProblems.plusOrMinus(a6)} ; {varName} = {ans}"
        else: 
            a2 = rd.randint(-10,10)
            a4 = a2 - coeff2

            a1 = rd.randint(-10,10)
            a3 = a1 - coeff1

            return f"{MathProblems.correctCoeff(a1,True)}{varName} {MathProblems.plusOrMinus(a2)} = {MathProblems.correctCoeff(a3,True)}{varName} {MathProblems.plusOrMinus(a4)} ; {varName} = {ans}"
        
    """Statistics"""

    def missingMean(varName: str, size: int):
        mean = rd.randint(-100,100)
        total = mean*size
        minToMax = [min(math.floor(.7*mean),math.floor(1.3*mean)),max(math.floor(.7*mean),math.floor(1.3*mean))]
        given = [rd.randrange(minToMax[0],minToMax[1]) for _ in range(size - 1)]
        ans = total - np.sum(given)
        shuffled = rd.sample(given + [varName], k=size)
        return f"If a list is given as {shuffled} with a mean of {mean}, what is {varName}? ; {varName} = {ans}"
    
    def findMedian(size: int):
        data = [rd.randrange(-100,100) for _ in range(size)]
        ans = statistics.median(data)
        return f"What is the median of the data set: {data}? ; ANSWER: {ans}"
    
    def findMean(size: int):
        ans = rd.randint(-100,100)
        total = ans*size
        minToMax = [min(math.floor(.7*ans),math.floor(1.3*ans)),max(math.floor(.7*ans),math.floor(1.3*ans))]
        given = [rd.randrange(minToMax[0],minToMax[1]) for _ in range(size - 1)]
        lastValue = total - np.sum(given)
        data = rd.sample(given + [lastValue],k=size)
        return f"What is the mean of the data set: {data}? ; ANSWER: {ans}"
    
print(MathProblems.twoSidedSingleVariable("x",3,False))