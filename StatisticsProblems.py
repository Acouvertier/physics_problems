import random as rd
import numpy as np
import statistics
import sympy as sp

"""
input: list of lists (sublists are the form [float,string])
output: a string where the contents are sorted using the float and the words are written with appropriate (in)equality signs
"""
def equality_order(lst:list[list]) -> str:
        if len(lst) == 0: 
            return ""
        elif len(lst) == 1: 
            return f"{lst[0][1]}"
        else: 
            sorted_list = sorted(lst,key= lambda x: x[0])
            if sorted_list[0][0] < sorted_list[1][0]:
                holder = f"{sorted_list[0][1]} < {sorted_list[1][1]}"
            else: # lst is sorted from small to large, so if lst[0] is not less, it must be equal
                holder = f"{sorted_list[0][1]} = {sorted_list[1][1]}"
            
            for i in range(len(sorted_list) - 2):
                if sorted_list[i+2][0] > sorted_list[i+1][0]:
                    holder += f" < {sorted_list[i+2][1]}"
                else: 
                    holder += f" = {sorted_list[i+2][1]}"
            return holder
        
def make_list_with_stats(min_value:float, max_value:float, list_size:int, need_mode:True) -> list[int]:
        if list_size < 3: 
            print("Insufficient size, must be greater than or equal to 3 in length. Updating to 3")
            list_size = 3
        
        full_list = [elt.item() for elt in rd.choices(np.linspace(min_value,max_value,sp.ceiling(4*(max_value-min_value)+1)),k=list_size)]
        mode = None
        
        if need_mode: 
            repeat_count = rd.randint(2,sp.ceiling(list_size/2))
            full_list = rd.sample(full_list, k = list_size - repeat_count)
            mode = rd.choice(np.linspace(min_value,max_value,sp.ceiling(4*(max_value-min_value)+1))).item()
            full_list += [mode for _ in range(repeat_count)]
        
        mean = round(statistics.mean(full_list),2)
        median = statistics.median(full_list)
        
        return [full_list, mean, median, mode]

def missingMean(varName: str, size: int):
        mean = rd.randint(-100,100)
        total = mean*size
        minToMax = [min(sp.floor(.7*mean),sp.floor(1.3*mean)),max(sp.floor(.7*mean),sp.floor(1.3*mean))]
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
    minToMax = [min(sp.floor(.7*ans),sp.floor(1.3*ans)),max(sp.floor(.7*ans),sp.floor(1.3*ans))]
    given = [rd.randrange(minToMax[0],minToMax[1]) for _ in range(size - 1)]
    lastValue = total - np.sum(given)
    data = rd.sample(given + [lastValue],k=size)
    return f"What is the mean of the data set: {data}? ; ANSWER: {ans}"


def statistics_problem(problem_type:int)->list[str]:
        

    if problem_type == 1:
       
        question_version = rd.choice([True,False]) #If True, list with missing element. If False, desired average word problem
        
        if question_version:
            min_value = 10
        else: 
            min_value = 70
        
        max_value = 100
        list_size = rd.randint(5,8)
        
        [full_list, mean, median, mode] = make_list_with_stats(min_value, max_value, list_size, rd.choice([True,False]))

        index_to_remove = rd.choice(range(list_size))
        answer = full_list[index_to_remove]
        full_list[index_to_remove] = 'x'
        
        choices = rd.sample([answer, answer + 1, answer - 1, mean, round(.8*answer,2)],k=5)
        
        if question_version:
            return [
                f"If the list {full_list} has a {rd.choice(["mean","average","arithmetic mean"])} of {mean}, what is the value of x?",
                f"A. {choices[0]}\nB. {choices[1]}\nC. {choices[2]}\nD. {choices[3]}\nE. {choices[4]}",
                f"ANSWER: {answer}"
            ]
        else: 
            full_list.pop(index_to_remove)
            return [
                f"Kelly is a sophomore in a physics course whose grading policy is solely based on test grades. For the semester, {list_size - 1} tests have been administered and she has earned {full_list}. There are a total of {list_size} graded test for the course, what grade does she need on the last test to earn an average of {mean}. (Assume all grades are out of 100 points and weighted equally)",
                f"A. {choices[0]}\nB. {choices[1]}\nC. {choices[2]}\nD. {choices[3]}\nE. {choices[4]}",
                f"ANSWER: {answer}"
            ]
    
    elif problem_type == 2:
       
        min_value = 10
        max_value = 50
        list_size = rd.randint(6,8)
        
        [full_list, mean, median, mode] = make_list_with_stats(min_value, max_value, list_size, True)

        correct_order = sorted([[mean,"mean"],[median,"median"],[mode,"mode"]],key= lambda x: x[0])

        return [
            f"Order the mean, median and mode of the list {full_list} from smallest to largest.",
            f"CORRECT: {equality_order(correct_order)}"
        ]
    
    elif problem_type == 3:

        min_value = 70
        max_value = 100
        list_size = rd.randint(6,8)
        
        [full_list, mean, median, mode] = make_list_with_stats(min_value, max_value, list_size, rd.choice([True,False]))

        
        removed_add_value = full_list.pop(rd.randint(0,list_size-1))
        
        small_mean = round(statistics.mean(full_list),2)

        question_version = rd.choice([True,False]) #True someone is added, False someone is removed
        choices = rd.sample([removed_add_value, removed_add_value - 1, removed_add_value + 1, removed_add_value * 2, removed_add_value - 2],k=5)

        if question_version:
            return [
                f"A group of {list_size - 1} students are selected so their average final exam grade is a {small_mean}. Another student unexpectedly comes into the room, which makes the rooms average final grade become {mean}. What was the final grade of the student who just entered the room?",
                f"A. {choices[0]}\nB. {choices[1]}\nC. {choices[2]}\nD. {choices[3]}\nE. {choices[4]}",
                f"ANSWER: {removed_add_value}"
            ]
        else:
            return [
                f"A group of {list_size} finalist body builders are choosen to compete in the final round of the National Body Building Competetion. Those selected have an average judge score of {mean}. Due to an injury, one of the finalist has to step down. Without this finalist the average judge score is now {small_mean}. What was the score of the injured body builder who dropped out?",
                f"A. {choices[0]}\nB. {choices[1]}\nC. {choices[2]}\nD. {choices[3]}\nE. {choices[4]}",
                f"ANSWER: {removed_add_value}"
            ]

print(f"{[1,2,3,4,5]} is a list")