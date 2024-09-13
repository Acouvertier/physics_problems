import random as rd
import numpy as np
import math
import statistics
from fractions import Fraction
import sympy as sym

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
    
    """Test Prep"""
    
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
    
    def namingTriangles():
        sides = ['equilateral','scalene','scalene','isosceles','isosceles']
        angles = ['right', 'acute', 'obtuse']
        
        ansSide = rd.choice(sides)
        

        if ansSide == 'equilateral':
            sides = [rd.randint(3,41)] * 3
            ansAngle = 'acute'
            return [f"A triangle is made of sides with lengths {sides[0]}, {sides[1]}, and {sides[2]}. What is the best description for this triangle",f"ANSWER: {ansSide} {ansAngle}"]
        elif ansSide == 'isosceles':
            sides = [rd.randint(3,41)]*2
            
        else:
            sides = rd.sample(range(3,41),k=2)
        
        ansAngle = rd.choice(angles)

        largestIndex = rd.choice([0,1,2])

        if largestIndex == 2:
            thirdSideBound = sym.sqrt(sides[0]**2 + sides[1]**2)
            if ansAngle == 'right':
                thirdSide = thirdSideBound
            elif ansAngle == 'obtuse': 
                thirdSideMaxBound = np.sum(sides)
                thirdSideMinBound = math.ceil(thirdSideBound.doit())
                thirdSide = rd.randrange(thirdSideMinBound,thirdSideMaxBound-1)
            else: 
                thirdSideMinBound = max(sides)
                thirdSideMaxBound = math.floor(thirdSideBound.doit())
                thirdSide = rd.randrange(thirdSideMinBound+1,thirdSideMaxBound)
        else:
            leftover = 0 if largestIndex == 1 else 1
            thirdSideBound = sym.sqrt(sides[largestIndex]**2 - sides[leftover]**2)
            if ansAngle == 'right':
                thirdSide = thirdSideBound
            elif ansAngle == 'acute': 
                thirdSideMaxBound = max(sides)
                thirdSideMinBound = math.ceil(thirdSideBound.doit())
                thirdSide = rd.randrange(thirdSideMinBound,thirdSideMaxBound-1)
            else: 
                thirdSideMinBound = max(sides) - min(sides)
                thirdSideMaxBound = math.floor(thirdSideBound.doit())
                thirdSide = rd.randrange(thirdSideMinBound+1,thirdSideMaxBound)

        sides.append(thirdSide)
        rd.shuffle(sides)
        
        return [f"A triangle is made of sides with lengths {sides[0]}, {sides[1]}, and {sides[2]}. What is the best description for this triangle",f"ANSWER: {ansSide} {ansAngle}"]

    def makeValidTriangle():
        sides = rd.choices(range(3,25),k=2)
        thirdLargest = rd.choice([True,False])
        if thirdLargest:
            minLen = max(sides) + 1
            maxLen = np.sum(sides) - 1
            sides.append(rd.randint(minLen,maxLen))
        else:
            minLen = max(sides) - min(sides) + 1 
            maxLen = max(sides) - 1
            sides.append(rd.randint(minLen,maxLen))
        
        return rd.sample(sides,k=len(sides))


        
 
print(MathProblems.makeValidTriangle())