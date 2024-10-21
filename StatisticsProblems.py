import random as rd
import numpy as np
import statistics
import sympy as sp
from collections import Counter
from fractions import Fraction

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

def missing_value_mean(varName: str, size: int):
        mean = rd.randint(-100,100)
        total = mean*size
        minToMax = [min(sp.floor(.7*mean),sp.floor(1.3*mean)),max(sp.floor(.7*mean),sp.floor(1.3*mean))]
        given = [rd.randrange(minToMax[0],minToMax[1]) for _ in range(size - 1)]
        ans = total - np.sum(given)
        shuffled = rd.sample(given + [varName], k=size)
        return f"If a list is given as {shuffled} with a mean of {mean}, what is {varName}? ; {varName} = {ans}"
    
def find_median(size: int):
    data = [rd.randrange(-100,100) for _ in range(size)]
    ans = statistics.median(data)
    return f"What is the median of the data set: {data}? ; ANSWER: {ans}"

def calculate_mean(size: int):
    ans = rd.randint(-100,100)
    total = ans*size
    minToMax = [min(sp.floor(.7*ans),sp.floor(1.3*ans)),max(sp.floor(.7*ans),sp.floor(1.3*ans))]
    given = [rd.randrange(minToMax[0],minToMax[1]) for _ in range(size - 1)]
    lastValue = total - np.sum(given)
    data = rd.sample(given + [lastValue],k=size)
    return f"What is the mean of the data set: {data}? ; ANSWER: {ans}"

def compare_3ms(min_val:int, max_val:int, list_size:int):
    
    [full_list, mean, median, mode] = make_list_with_stats(min_val, max_val, list_size, True)

    correct_order = sorted([[mean,"mean"],[median,"median"],[mode,"mode"]],key= lambda x: x[0])

    return [
        f"Order the mean, median and mode of the list {full_list} from smallest to largest.",
        f"CORRECT: {equality_order(correct_order)}"
    ]
     
def updated_mean(min_val:int,max_val:int,list_size:int, add_remove:bool):
    
    
    [full_list, mean, median, mode] = make_list_with_stats(min_val, max_val, list_size, rd.choice([True,False]))

    
    removed_add_value = full_list.pop(rd.randint(0,list_size-1))
    
    small_mean = round(statistics.mean(full_list),2)

    question_version = add_remove #True someone is added, False someone is removed
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
    
def create_categories():
    keys = rd.choice([["red","green","black"],["tie dye", "plain black", "stripped"]])
    categories_dict = {}
    for key in keys:
        categories_dict[key] = rd.randint(1,10)

    return categories_dict

def create_int_list():
    list_of_ints = rd.choices(range(1,11),k=rd.randint(6,10))

    return Counter(list_of_ints)

def make_int_list(int_dict:Counter):

    holder = []
    for key,value in int_dict.items():
        holder += (value * [key])
    rd.shuffle(holder)
    return holder
        
def single_selection_probability(list_or_categories:bool):
    if list_or_categories: #True provide categories, False provide list of integers
        categories_dict = create_categories()
        keys = list(categories_dict.keys())
        total = sum(categories_dict.values())
        ans = rd.choice(keys)
        ans_prob = Fraction(categories_dict[ans],total)

        beginning = f"A collection of {categories_dict[keys[0]]} {keys[0]}, {categories_dict[keys[1]]} {keys[1]}, and {categories_dict[keys[2]]} {keys[2]} marbles"
        
    
    else: 
        int_dict = create_int_list()
        keys = list(int_dict.keys())
        ans = rd.choice(keys)
        total = sum(int_dict.values())
        ans_prob = Fraction(int_dict[ans],total)

        beginning = f"A list with digits {make_int_list(int_dict)}"
    
    extra_string = ""
    if rd.choice([True,False]): #True ask for NOT probability, else regular
        ans_prob = Fraction(1 - ans_prob).limit_denominator()
        extra_string = " NOT"
    
    return f"{beginning} is provided. What is the probability that a person will{extra_string} select a {ans}? ANSWER: {ans_prob}"


def double_selection_probability(list_or_categories:bool, and_or:bool):
    
    problem_dict = create_categories() if list_or_categories else create_int_list()
    keys = list(problem_dict.keys())
    total = sum(problem_dict.values())

    extra_string = ""

    if and_or: #True is "and then", False is "or"
        [key_A, key_B] = rd.choices(list(problem_dict.keys()),k=2)

        if rd.choice([True,False]): #True means no replacement, False means replacement
            extra_string = "without replacement "
            first_grab = problem_dict[key_A]
            second_grab = problem_dict[key_B] if key_A != key_B else problem_dict[key_B] - 1
            ans_prob = Fraction((first_grab * second_grab),(total*(total-1))).limit_denominator()
        else: 
            extra_string = "with replacement "
            first_grab = problem_dict[key_A]
            second_grab = problem_dict[key_B] if key_A != key_B else problem_dict[key_B] - 1
            ans_prob = Fraction((first_grab * second_grab),(total*total)).limit_denominator()
    else: 
        [key_A, key_B] = rd.sample(list(problem_dict.keys()),k=2)
        first_grab = problem_dict[key_A]
        second_grab = problem_dict[key_B]
        ans_prob = Fraction((first_grab + second_grab),(total)).limit_denominator()

    if list_or_categories:
        beginning = f"A collection of {problem_dict[keys[0]]} {keys[0]}, {problem_dict[keys[1]]} {keys[1]}, and {problem_dict[keys[2]]} {keys[2]} marbles"
    else: 
        beginning = f"A list with digits {make_int_list(problem_dict)}"

    return f"{beginning} is provided. What is the probability that one selects {key_A} {"and then" if and_or else "or"} {key_B} {extra_string}? ANSWER: {ans_prob}"
        
def expected_value_frequency_table():
    pass

print(double_selection_probability(True, True))