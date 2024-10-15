import random as rd
import numpy as np
import math
import statistics
from fractions import Fraction
import sympy as sym

#problem_type = range(1,5)
def sequence_problem(problem_type:int) -> list[str]:
    a1 = rd.randint(-10,10)
    d = Fraction(rd.choice(list(np.linspace(-10,-0.5,39))+list(np.linspace(0.5,10,39)))).limit_denominator()
    if problem_type == 1:
        [n,m,r] = rd.sample(range(3,12),k=3)
        an = a1 + (n-1)*d
        am = a1 + (m-1)*d
        choices = rd.sample([a1, a1 + (r)*d, a1 + (r+1)*d, a1 + d, a1 + (r-1)*d],k=5)
        return [
            f"The terms in an arithmatic sequence at locations {n} and {m} are {an} and {am} respectively. What is the value of the term at location {r}?",
            f"A. {choices[0]}\nB.{choices[1]} \nC. {choices[2]}\nD. {choices[3]}\nE. {choices[4]}",
            f"ANSWER: {a1 + (r-1)*d}"
        ]
    
    elif problem_type == 2:
        [m,l] = rd.sample(range(2,12),k=2)
        am = a1 + (m-1)*d
        choices = rd.sample([a1 + (l-1)*d, a1 ,a1 + (l)*d, a1 + (l+1)*d,a1 + (l+2)*d],k=5)
        return [
            f"An arithmetic sequence has a common difference of {d}. If the term at position {m} is {am}, what is the term at position {l}?",
            f"A. {choices[0]}\nB.{choices[1]} \nC. {choices[2]}\nD. {choices[3]}\nE. {choices[4]}",
            f"ANSWER: {a1 + (l-1)*d}"
        ]


    elif problem_type == 3: 
        m = rd.randint(3,12)
        sum_list = [(index*(2*a1+(index-1)*d))/2 for index in [m,m+1,m-1,1,m+2]]
        choices = rd.sample(sum_list,k=5)

        return [
            f"What is the sum of the first {m} terms in the arithmetic sequence defined as aₙ = {a1} + (n-1)({d})",
            f"A. {choices[0]}\nB.{choices[1]} \nC. {choices[2]}\nD. {choices[3]}\nE. {choices[4]}",
            f"ANSWER: {sum_list[0]}"
        ]
    
    elif problem_type == 4: 
        m = rd.randint(3,12)
        sum_list = [(index*(2*a1+(index-1)*d))/2 for index in [m,m+1,m-1,1,m+2]]
        choices = rd.sample(sum_list,k=5)
        [n,q] = rd.sample(range(3,12),k=2)
        an = a1 + (n-1)*d
        aq = a1 + (q-1)*d
        return [
            f"What is the sum of the first {m} terms in an arithmetic sequence if the terms at locations {n} and {q} are {an} and {aq}?",
            f"A. {choices[0]}\nB.{choices[1]} \nC. {choices[2]}\nD. {choices[3]}\nE. {choices[4]}",
            f"ANSWER: {sum_list[0]}"
        ]

#problem_type = range(1,5)
def geometry_problem(problem_type: int) -> list[str]:
    perimeter_solve_dict = {
        "square": lambda x: round(4*x,2),
        "triangle": lambda x: round(3*x,2),
        "circle": lambda x: round(2 * math.pi * x,2),
        "rectangle": lambda x,y: 2*x + 2*y
    }
    
    parameter_solve_dict = {
        "square": lambda x: round(x/4,2),
        "triangle": lambda x: round(x/3,2),
        "circle": lambda x: round(x/(2*math.pi),2),
        "rectangle": lambda x,y: round(x/y,2)
    }

    parameter_solve_dict_area = {
        "square": lambda A: round(math.sqrt(A),2),
        "circle": lambda A: round(math.sqrt(A / math.pi),2),
        "rectangle": lambda A,l: round(A/l, 2),
        "triangle": lambda A,b: round(2*A / b, 2)
    }
    
    area_solve_dict = {
        "square": lambda s: round(s**2,2),
        "circle": lambda r: round(math.pi * r**2,2),
        "rectangle": lambda l,w: round(l*w),
        "triangle": lambda b,h: round(0.5*b*h,2)
    }

    volume_solve_dict = {
        "cube": lambda s: round(s**3,2),
        "sphere": lambda r: round(math.pi * (4/3) * r**3,2),
        "prism": lambda l, w, h: round(l*w*h),
        "cylinder": lambda r, h: round(math.pi * (r**2) * h,2)
    }

    parameter_solve_dict_volume = {
        "cube": lambda V: round(math.pow(V,1/3),2),
        "sphere": lambda V: round(math.pow(V / (math.pi * (4/3)),1/3),2),
        "prism": lambda V, w, h: round(V/(w*h),2),
        "cylinder": lambda V, h: round(math.pow(V/(math.pi * h), 1/2),2)
    }
    
    units = ["cm","m","mm","ft","mi","in","km"]

    def write_paramaters(parameters, units):
            if len(parameters) == 1:
                return f"{parameters[0]} {units}"
            else:
                holder = ""
                for i in range(len(parameters)):
                    if i == len(parameters) - 1:
                        holder += f"and {parameters[i]} {units}"
                    else:
                        holder += f"{parameters[i]} {units}, "
                return holder
    
    if problem_type == 1:
        [start_shape, end_shape] = rd.sample(["square","triangle","circle"],k=2)
        shape_key = {
            "square": ["square", "side length"],
            "triangle": ["equilateral triangle","side length"],
            "circle": ["circle", "radius"]}
        given_units = rd.choice(units)
        start_parameter = rd.randint(2,80)
        start_perimeter = perimeter_solve_dict[start_shape](start_parameter)
        end_parameter = parameter_solve_dict[end_shape](start_perimeter)
        choices = rd.sample([end_parameter,start_perimeter,round(0.5*end_parameter,2),2*start_perimeter,end_parameter+1],k=5)
        return [
            f"A thin metal wire is formed into a {shape_key[start_shape][0]} with a {shape_key[start_shape][1]} of {start_parameter} {given_units}. The wire is repurposed into a {shape_key[end_shape][0]}, while no extra wire is removed or added. What is the {shape_key[end_shape][1]} of the new {end_shape}?",
            f"A. {choices[0]} {given_units}\nB. {choices[1]} {given_units}\nC. {choices[2]} {given_units}\nD. {choices[3]} {given_units}\nE. {choices[4]} {given_units}",
            f"ANSWER: {end_parameter} {given_units}"
        ]
    
    elif problem_type == 2:
        [big_shape, small_shape] = rd.sample(["square","circle","rectangle"],k=2)
        
        shape_key = {
            "square": ["cube","side length"],
            "rectangle": ["prism","length and width"],
            "circle": ["sphere","radius"],
            "prism": ["prism","length, width, and height"],
            "cube": ["cube", "side length"],
            "sphere": ["sphere","radius"]
            }
        
        use_3D = rd.choice([True,False])
        given_units = rd.choice(["cm","mm","in"])
        
        if use_3D:
            [big_shape,small_shape] = [shape_key[big_shape][0],shape_key[small_shape][0]]
        
        if big_shape != 'rectangle' and big_shape != "prism":
            big_parameters = [rd.choice(np.linspace(10,21,45))]
            big_value = volume_solve_dict[big_shape](big_parameters[0]) if use_3D else area_solve_dict[big_shape](big_parameters[0])
        elif big_shape == 'rectangle':
            big_parameters = rd.sample(list(np.linspace(10,21,45)),k=2)
            big_value = area_solve_dict[big_shape](big_parameters[0],big_parameters[1])
        else:
            big_parameters = rd.sample(list(np.linspace(10,21,45)),k=3)
            big_value = volume_solve_dict[big_shape](big_parameters[0],big_parameters[1],big_parameters[2])
        
        if small_shape != 'rectangle' and small_shape != "prism":
            small_parameters = [rd.choice(np.linspace(1,5,17))]
            small_value = volume_solve_dict[small_shape](small_parameters[0]) if use_3D else area_solve_dict[small_shape](small_parameters[0])
        elif small_shape == 'rectangle':
            small_parameters = rd.sample(list(np.linspace(1,5,17)),k=2)
            small_value = area_solve_dict[small_shape](small_parameters[0],small_parameters[1])
        else:
            small_parameters = rd.sample(list(np.linspace(1,5,17)),k=3)
            small_value = volume_solve_dict[small_shape](small_parameters[0],small_parameters[1],small_parameters[2])

        correct = round(big_value - small_value,2)
        choices = rd.sample([correct,round(big_value,2),round(1.2*small_value,2),round(big_value+small_value,2),round(correct*1.2,2)],k=5)

        return [
            f"In a certain factory, the {rd.choice(["lollipop","candy"])} mold is effectively a {big_shape} with a {shape_key[big_shape][1]} of {write_paramaters(big_parameters,given_units)}. Before the molds are filled with candy, a small chocolate center is added. The chocolate center for this promotion is a {small_shape}. If the chocolate has a {shape_key[small_shape][1]} of {write_paramaters(small_parameters,given_units)}, what is the {"volume" if use_3D else "area"} of candy needed to fill the mold?",
            f"A. {choices[0]} {given_units}{"³" if use_3D else "²"}\nB. {choices[1]} {given_units}{"³" if use_3D else "²"}\nC. {choices[2]} {given_units}{"³" if use_3D else "²"}\nD. {choices[3]} {given_units}{"³" if use_3D else "²"}\nE. {choices[4]} {given_units}{"³" if use_3D else "²"}",
            f"ANSWER: {correct} {given_units}{"³" if use_3D else "²"}"
        ]
    
    elif problem_type == 3:
        
        out_shape = rd.choice(["square","circle"])
        in_shape = "circle" if out_shape == "square" else rd.choice(['square','rectangle'])

        shape_key = {
            "square": "side length",
            "circle": "radius", 
            "rectangle": "length and width"
        }

        out_shape_parameter = rd.choice(list(np.linspace(0.25, 20.25,81)))
        out_shape_area = area_solve_dict[out_shape](out_shape_parameter)
        out_shape_perimeter = perimeter_solve_dict[out_shape](out_shape_parameter)
        out_shape_value = rd.choice([["area",out_shape_area],["perimeter",out_shape_perimeter]])
        
        if in_shape == "square": #out_shape has to be circle
            in_shape_parameters = [(out_shape_parameter*2)/(math.sqrt(2))]
            in_shape_value = rd.choice([["area",area_solve_dict[in_shape](in_shape_parameters[0])],["perimeter",perimeter_solve_dict[in_shape](in_shape_parameters[0])]])
        elif in_shape == "circle": #out_shape has to be square
            in_shape_parameters = [out_shape_parameter/2]
            in_shape_value = rd.choice([["area",area_solve_dict[in_shape](in_shape_parameters[0])],["perimeter",perimeter_solve_dict[in_shape](in_shape_parameters[0])]])
        else: # in_shape is rectangle
            in_shape_parameters = [out_shape_parameter, math.sqrt(3)*out_shape_parameter]
            in_shape_value = rd.choice([["area",area_solve_dict[in_shape](in_shape_parameters[0],in_shape_parameters[1])],["perimeter",perimeter_solve_dict[in_shape](in_shape_parameters[0],in_shape_parameters[1])]])

        correct = round(in_shape_value[1],2)
        choices = rd.sample([correct,round(in_shape_parameters[0],2),round(out_shape_parameter,2),round(correct-1,2),round(correct*1.2,2)],k=5)
        given_units = rd.choice(units)
        return [
            f"A {out_shape} inscribes a {in_shape}. {"The diagnoal of the rectangle is twice the length of its smaller side. " if in_shape == 'rectangle' else ''}If the {out_shape_value[0]} for the {out_shape} is {out_shape_value[1]} {given_units}{"" if out_shape_value[0]=="perimeter" else "²"}, what is the {in_shape_value[0]} of the {in_shape}?",
            f"A. {choices[0]} {given_units}{"" if in_shape_value[0]=="perimeter" else "²"}\nB. {choices[1]} {given_units}{"" if in_shape_value[0]=="perimeter" else "²"}\nC. {choices[2]} {given_units}{"" if in_shape_value[0]=="perimeter" else "²"}\nD. {choices[3]} {given_units}{"" if in_shape_value[0]=="perimeter" else "²"}\nE. {choices[4]} {given_units}{"" if in_shape_value[0]=="perimeter" else "²"}",
            f"ANSWER: {correct} {given_units}{"" if in_shape_value[0]=="perimeter" else "²"}"
        ]
            

    elif problem_type == 4:
        [big_shape, small_shape] = rd.sample(["square","circle","rectangle"],k=2)
        
        shape_key = {
            "square": ["cube","side length"],
            "rectangle": ["prism","length and width"],
            "circle": ["sphere","radius"],
            "prism": ["prism","length, width, and height"],
            "cube": ["cube", "side length"],
            "sphere": ["sphere","radius"]
            }
        
        use_3D = rd.choice([True,False]) #True makes the problem use 3D shapes
        

        if use_3D:
            [big_shape,small_shape] = [shape_key[big_shape][0],shape_key[small_shape][0]]
        
        if big_shape != 'rectangle' and big_shape != "prism":
            big_parameters = [rd.choice(np.linspace(10,21,45))]
            big_value = volume_solve_dict[big_shape](big_parameters[0]) if use_3D else area_solve_dict[big_shape](big_parameters[0])
        elif big_shape == 'rectangle':
            big_parameters = rd.sample(list(np.linspace(10,21,45)),k=2)
            big_value = area_solve_dict[big_shape](big_parameters[0],big_parameters[1])
        else:
            big_parameters = rd.sample(list(np.linspace(10,21,45)),k=3)
            big_value = volume_solve_dict[big_shape](big_parameters[0],big_parameters[1],big_parameters[2])
        
        number_used = rd.choice(np.linspace(0.5,65.5,131))
        small_value = big_value/number_used

        if small_shape != 'rectangle' and small_shape != "prism":
            small_parameters = [parameter_solve_dict_volume[small_shape](small_value) if use_3D else parameter_solve_dict_area[small_shape](small_value)]
        elif small_shape == 'rectangle':
            fixed_value = rd.choice(np.linspace(3,7,17))
            small_parameters = [parameter_solve_dict_area[small_shape](small_value,fixed_value),fixed_value]
        else:
            fixed_values = rd.sample(list(np.linspace(3,7,17)),k=2)
            small_parameters = [parameter_solve_dict_volume[small_shape](small_value,fixed_values[0],fixed_values[1])] + fixed_values

        correct = math.ceil(number_used)
        choices = rd.sample([correct,correct-1,math.floor(1.2*correct),math.ceil(0.8*correct),math.ceil(2*correct)],k=5)
        given_units = rd.choice(["in","mm","cm","ft"])
        return [
            f"Will is a first-year student in an accelerated art course. For his midterm project he must create a clay sculpture in the shape of a {big_shape} with a {shape_key[big_shape][1]} of {write_paramaters(big_parameters,given_units)}. Going to the local art supply store, he finds the clay is only sold in cases shaped like {small_shape} with a {shape_key[small_shape][1]} or {write_paramaters(small_parameters,given_units)}. How many cases should Will buy to complete his project?",
            f"A. {choices[0]}\nB. {choices[1]}\nC. {choices[2]}\nD. {choices[3]}\nE. {choices[4]}",
            f"ANSWER: {correct}"
        ]

#problem_type = range(1,4)    
def statistics_problem(problem_type:int)->list[str]:

    def list_with_commas(lst):
        if len(lst) == 0:
            return ""
        elif len(lst) == 1:
            return f"{lst[0]}"
        else: 
            holder = ""
            for i in range(len(lst)-1):
                holder += f"{lst[i]}, "
            holder += f"and {lst[-1]}"
            return holder
    
    def equality_order(lst):
        if len(lst) == 0: 
            return ""
        elif len(lst) == 1: 
            return f"{lst[0][1]}"
        else: 
            if lst[0][0] < lst[1][0]:
                holder = f"{lst[0][1]} < {lst[1][1]}"
            else: # lst is sorted from small to large, so if lst[0] is not less, it must be equal
                holder = f"{lst[0][1]} = {lst[1][1]}"
            
            for i in range(len(lst) - 2):
                if lst[i+2][0] > lst[i+1][0]:
                    holder += f" < {lst[i+2][1]}"
                else: 
                    holder += f" = {lst[i+2][1]}"
            return holder
        
    def make_list_with_stats(min_value:float, max_value:float, list_size:int, need_mode:True) -> list[int]:
        if list_size < 3: 
            print("Insufficient size, must be greater than or equal to 3 in length.")
        
        full_list = [elt.item() for elt in rd.choices(np.linspace(min_value,max_value,math.ceil(4*(max_value-min_value)+1)),k=list_size)]
        mode = None
        
        if need_mode: 
            repeat_count = rd.randint(2,math.ceil(list_size/2))
            full_list = rd.sample(full_list, k = list_size - repeat_count)
            mode = rd.choice(np.linspace(min_value,max_value,math.ceil(4*(max_value-min_value)+1))).item()
            full_list += [mode for _ in range(repeat_count)]
        
        mean = round(statistics.mean(full_list),2)
        median = statistics.median(full_list)
        
        return [full_list, mean, median, mode]
        

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
                f"Kelly is a sophomore in a physics course whose grading policy is solely based on test grades. For the semester, {list_size - 1} tests have been administered and she has earned {list_with_commas(full_list)}. There are a total of {list_size} graded test for the course, what grade does she need on the last test to earn an average of {mean}. (Assume all grades are out of 100 points and weighted equally)",
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
            f"Order the mean, median and mode of the list [{list_with_commas(full_list)}] from smallest to largest.",
            f"CORRECT: {equality_order(correct_order)}"
        ]
    
    elif problem_type == 3:

        min_value = 70
        max_value = 100
        list_size = rd.randint(6,8)
        
        [full_list, mean, median, mode] = make_list_with_stats(min_value, max_value, list_size, rd.choice([True,False]))

        big_list = full_list[::]
        removed_add_value = full_list.pop(rd.randint(0,list_size-1))
        small_list = full_list
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






        

        
        



print(statistics_problem(rd.randint(1,3)))#problem_type = range(1,5)
print("____________________________________\n")
print(geometry_problem(4))#problem_type = range(1,5)
print("____________________________________\n")
print(sequence_problem(rd.randint(1,4)))#problem_type = range(1,4)