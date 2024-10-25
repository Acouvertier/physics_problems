import random as rd
import math
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

def missing_value_mean(varName:str, size:int):
    mean = rd.randint(-100,100)
    total = mean*size
    minToMax = [min(sp.floor(.7*mean),sp.floor(1.3*mean)),max(sp.floor(.7*mean),sp.floor(1.3*mean))]
    given = [rd.randrange(minToMax[0],minToMax[1]) for _ in range(size - 1)]
    ans = total - np.sum(given)
    shuffled = rd.sample(given + [varName], k=size)
    return f"I have the following list: {shuffled} where {varName} is an unknown value. Create a real-life scenario word problem (standardized test-style), that asks the student to find the value of {varName}. The answer is {ans}, include other answer choices that are distinct and serve as distractors."
    
def find_median(size:int):
    data = [rd.randrange(-100,100) for _ in range(size)]
    ans = statistics.median(data)
    return f"I have the following list: {data}. Create a real-life scenario word problem (standardized test-style), that asks the student to find the median of the list. The answer is {ans}, include other answer choices that are distinct and serve as distractors."

def calculate_mean(size:int):
    ans = rd.randint(-100,100)
    total = ans*size
    minToMax = [min(sp.floor(.7*ans),sp.floor(1.3*ans)),max(sp.floor(.7*ans),sp.floor(1.3*ans))]
    given = [rd.randrange(minToMax[0],minToMax[1]) for _ in range(size - 1)]
    lastValue = total - np.sum(given)
    data = rd.sample(given + [lastValue],k=size)
    return f"I have the following list: {data}. Create a real-life scenario word problem (standardized test-style), that asks the student to find the mean of the list. The answer is {ans}, include other answer choices that are distinct and serve as distractors."

def compare_3ms(min_val:int, max_val:int, list_size:int):
    
    [full_list, mean, median, mode] = make_list_with_stats(min_val, max_val, list_size, True)

    correct_order = sorted([[mean,"mean"],[median,"median"],[mode,"mode"]],key= lambda x: x[0])

    return f"I have a Python list of numbers, and I would like to create a real-life scenario (such as comparing student grades, prices, or measurements) that asks the student to compare the values of the mean, median, and mode of the list. The question should guide the student to determine which of these measures is greatest or smallest. I will also provide the correct answer. Please generate the scenario and include multiple-choice options. Here is the list: {full_list}. The correct answer is {equality_order(correct_order)}."
     
def updated_mean(min_val:int, max_val:int, list_size:int, add_remove:bool):
    
    [full_list, mean, median, mode] = make_list_with_stats(min_val, max_val, list_size, rd.choice([True,False]))
    
    removed_add_value = full_list.pop(rd.randint(0,list_size-1))
    mean = round(mean,2)
    small_mean = round(statistics.mean(full_list),2)

    return f"I have a list of numbers with {list_size -1 if add_remove else list_size} digits, and I know the mean of this list is {small_mean if add_remove else mean}. I also know the updated mean after a digit is {"added" if add_remove else "removed"} becomes {mean if add_remove else small_mean}. Using this information, create a real-life scenario (such as student test scores, prices, etc.) and form a standardized test-style multiple-choice question. The question should ask what the missing or added data point is, based on the change in the mean. Provide distinct multiple-choice answers, including the correct answer of {removed_add_value}."
    
def create_single_data():
    keys = [f"category {i}" for i in range(1,rd.randint(4,7))]

    categories_dict = {}
    for key in keys:
        categories_dict[key] = rd.randint(1,15)

    return categories_dict
        
def single_selection_probability(include_not:bool):
    
    question_dict = create_single_data()
    keys = list(question_dict.keys())
    ans = rd.choice(keys)
    total = sum(question_dict.values())
    ans_prob = Fraction(question_dict[ans],total)

    add_not = " NOT" if include_not else ""
    ans_prob = 1 - ans_prob if include_not else ans_prob

    return f"Given the following dictionary of counts (the values) for different categories (the keys): {question_dict}. Create real-life scenario where these categories have meaning, and then form an standardized test -style multiple-choice question. The question should indirectly ask to find the probability that {ans} is{add_not}{" (Use the NOT keyword in the question)" if include_not else ""} selected at random for a single draw. The answer is {ans_prob}. Remove references to the categories after you make the scenario, do not explain the mapping, and ensure the other choices are distinct (not equal to the answer)."

def double_selection_probability(and_or:bool, no_replacements:bool):
    
    problem_dict = create_single_data()
    keys = list(problem_dict.keys())
    total = sum(problem_dict.values())

    extra_string = ""

    if and_or: #True is "and then", False is "or"
        [key_A, key_B] = rd.choices(keys,k=2)

        if no_replacements: #True means no replacement, False means replacement
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
        [key_A, key_B] = rd.sample(keys,k=2)
        first_grab = problem_dict[key_A]
        second_grab = problem_dict[key_B]
        ans_prob = Fraction((first_grab + second_grab),(total)).limit_denominator()

    return f"Given the following dictionary of counts (the values) for different categories (the keys): {problem_dict}. Create real-life scenario where these categories have meaning, and then form an standardized test -style multiple-choice question. The question should indirectly ask to find the probability that one selects {key_A} {"and then" if and_or else "or"} {key_B} {extra_string}? The ANSWER is: {ans_prob}. Remove references to the categories after you make the scenario, do not explain the mapping, and ensure the other choices are distinct (not equal to the answer)."
        
def counting_principle(cat_or_digits:bool):
    
    if cat_or_digits:
        my_scenario = create_single_data()
        ans = math.prod(my_scenario.values())
        return f"I have a Python dictionary with category names as keys and the number of choices in each category as the values. Each category represents a distinct choice, and I want to form a real-life scenario (such as selecting outfits, building a meal, or configuring a product) that uses the counting principle. The question should ask the student to find the total number of unique combinations when only one choice is made per category. Please ensure the multiple-choice options include the correct answer, {ans}, and distinct distractor answers. Here is the dictionary: {my_scenario}. Please create the question and provide distinct answer choices. Remove all references to the original categories when writing the word problem."
    else: 
        my_scenario = rd.choices(range(1,10),k=rd.randint(3,8))
        my_scenario_counter = Counter(my_scenario)
        bottom_factorials = np.prod([math.factorial(elt) for elt in my_scenario_counter.values()])
        ans = math.factorial(len(my_scenario))//bottom_factorials
        return f"I have a Python list of digits (with repeats) that will be used to create a number of length {len(my_scenario)}. Please create a real-life scenario (such as forming a code, generating a password, or setting a combination) where the student is asked to find how many unique numbers can be created using the given digits. Make sure the student is only allowed to use the provided digits for each position of the number. Include distinct multiple-choice options, and the correct answer is {ans}. Here is the list of digits: {my_scenario}, and the number of digits in the number to be formed is {len(my_scenario)}."
    
def two_way_table(): 
    n=rd.randint(2,4)
    m=rd.randint(2,4)
    column_headers = [[f"category {i}" for i in range(1,n+1)]]
    column_headers[0].append("total")
    column_headers[0].insert(0,None)
    row_headers = [f"category {i}" for i in range(n+1,n+m+1)]
    fake_data = np.random.randint(10,250,size=(m,n)).tolist()
    column_headers += fake_data
    
    for index in range(1,len(column_headers)):
        column_headers[index].append(sum(column_headers[index]))
        column_headers[index].insert(0,row_headers[index-1])

    last_row = ["total"]

    for index in range(1,len(column_headers[0])):
        column = [row[index] for row in column_headers][1:]
        last_row.append(sum(column))

    column_headers.append(last_row)
    
    if rd.choice([True,False]): #True adds conditional
        [prob,cond] = rd.sample([rd.choice(range(1,n+1)),rd.choice(range(n+1,n+m+1))],k=2)
    else: 
        prob = rd.choice(range(1,n+m+1))
        cond = -1

    if (prob > n) and cond != -1:
        numerator = column_headers[prob-n][cond]
        denominator = column_headers[-1][cond]
    elif (prob <= n) and cond != -1:
        numerator = column_headers[cond-n][prob]
        denominator = column_headers[cond-n][-1]
    elif (prob > n):
        numerator = column_headers[prob-n][-1]
        denominator = column_headers[-1][-1]
    elif (prob <= n):
        numerator = column_headers[-1][prob]
        denominator = column_headers[-1][-1]

    return f"Given the two way table for different categories, {column_headers}. Create a real-life scenario where these categories have meaning, and then form an standardized test -style multiple-choice question. The question should indirectly ask to find the probability that a randomly selected person is in category {prob}{f" given this person is also in category {cond}" if cond != -1 else ""}. Here is the ANSWER: {Fraction(numerator,denominator).limit_denominator()}. Remove references to the categories after you make the scenario, do not explain the mapping, and ensure the other choices are distinct (not equal to the answer)."