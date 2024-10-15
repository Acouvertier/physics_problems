import random as rd
import numpy as np
import sympy as sp
from Helpers import write_paramaters, random_non_zero_int, make_letter_choices

perimeter_solve_dict = {
        "square": lambda s: round(4*s,2),
        "triangle": lambda s: round(3*s,2), #equilateral
        "circle": lambda r: round(2 * sp.pi * r,2),
        "rectangle": lambda l,w: 2*l + 2*w
    }

area_solve_dict = {
        "square": lambda s: round(s**2,2),
        "circle": lambda r: round(sp.pi * r**2,2),
        "rectangle": lambda l,w: round(l*w),
        "triangle": lambda b,h: round(0.5*b*h,2)
    }

volume_solve_dict = {
        "cube": lambda s: round(s**3,2),
        "sphere": lambda r: round(sp.pi * (4/3) * r**3,2),
        "prism": lambda l, w, h: round(l*w*h),
        "cylinder": lambda r, h: round(sp.pi * (r**2) * h,2)
    }
    
parameter_solve_dict_perimeter = {
        "square": lambda P: round(P/4,2),
        "triangle": lambda P: round(P/3,2), #equilateral
        "circle": lambda C: round(C/(2*sp.pi),2),
        "rectangle": lambda P,l: round(P-2*l,2)
    }

parameter_solve_dict_area = {
        "square": lambda A: round(sp.sqrt(A),2),
        "circle": lambda A: round(sp.sqrt(A / sp.pi),2),
        "rectangle": lambda A,l: round(A/l, 2),
        "triangle": lambda A,b: round(2*A / b, 2)
    }

parameter_solve_dict_volume = {
        "cube": lambda V: round(sp.pow(V,1/3),2),
        "sphere": lambda V: round(sp.pow(V / (sp.pi * (4/3)),1/3),2),
        "prism": lambda V, w, h: round(V/(w*h),2),
        "cylinder": lambda V, h: round(sp.pow(V/(sp.pi * h), 1/2),2)
    }
    
small_units = ["in","cm","mm"]
big_units = ["ft","yd","mi","km"]

#TODO: Add difficulty and problem_type PARAMETERS to these functions to allow customization.

def remake_shape():
    [start_shape, end_shape] = rd.sample(["square","triangle","circle"],k=2)
    shape_dict = {
        "square": ["square", "side length"],
        "triangle": ["equilateral triangle","side length"],
        "circle": ["circle", "radius"]
    }

    given_units = rd.choice(small_units+big_units)

    
    start_parameters = [random_non_zero_int(16,True)]
    start_perimeter = perimeter_solve_dict[start_shape](start_parameters[0])
    
    
    
    end_parameters = [parameter_solve_dict_perimeter[end_shape](start_perimeter)]
    

    return f"You are creating the problems for a standardized math test. Write a(n) {rd.choice(["direct-concept", "application-based", "real-life"])} word problem that would be {rd.choice(["easy","moderate","difficult"])} for the average student. Provide an original shape of a(n) {start_shape} with a {shape_dict[start_shape][1]} of {write_paramaters(start_parameters,given_units)}. The shape should be deformed into a {shape_dict[end_shape][0]} of {write_paramaters(end_parameters,given_units)}. The student must solve for dimensions of the final shape, assuming conserved perimeter, ask for this in a(n) {rd.choice(["direct","indirect"])} fashion. The correct answer is {write_paramaters(end_parameters,given_units)}"
    
def leftover_volume_or_area():
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

    return f"You are creating the problems for a standardized math test. Write a(n) {rd.choice(["direct-concept", "application-based", "real-life"])}  word problem that would be {rd.choice(["easy","moderate","difficult"])} for the average student. Provide a bigger shape of a(n) {big_shape} with a {shape_key[big_shape][1]} of {write_paramaters(big_parameters,given_units)}. Inside is a smaller shape that is {small_shape} with a {shape_key[small_shape][1]} of {write_paramaters(small_parameters,given_units)}. The student must solve for the remaining {"volume" if use_3D else "area"}, ask for this in a(n) {rd.choice(["direct","indirect"])} fashion. Use the answer choices {make_letter_choices(choices)}."

def inscribed_shape():
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
        in_shape_parameters = [(out_shape_parameter*2)/(sp.sqrt(2))]
        in_shape_value = rd.choice([["area",area_solve_dict[in_shape](in_shape_parameters[0])],["perimeter",perimeter_solve_dict[in_shape](in_shape_parameters[0])]])
    elif in_shape == "circle": #out_shape has to be square
        in_shape_parameters = [out_shape_parameter/2]
        in_shape_value = rd.choice([["area",area_solve_dict[in_shape](in_shape_parameters[0])],["perimeter",perimeter_solve_dict[in_shape](in_shape_parameters[0])]])
    else: # in_shape is rectangle
        in_shape_parameters = [out_shape_parameter, sp.sqrt(3)*out_shape_parameter]
        in_shape_value = rd.choice([["area",area_solve_dict[in_shape](in_shape_parameters[0],in_shape_parameters[1])],["perimeter",perimeter_solve_dict[in_shape](in_shape_parameters[0],in_shape_parameters[1])]])

    correct = round(in_shape_value[1],2)
    choices = rd.sample([correct,round(in_shape_parameters[0],2),round(out_shape_parameter,2),round(correct-1,2),round(correct*1.2,2)],k=5)
    given_units = rd.choice(big_units+small_units)

    return f"You are creating the problems for a standardized math test. Write a(n) {rd.choice(["direct-concept", "application-based (Be creative with the scenario)", "real-life (Be creative with the scenario)"])}  word problem that would be {rd.choice(["easy","moderate","difficult"])} for the average student. Provide an outer shape of a(n) {out_shape} with a {out_shape_value[0]} of {write_paramaters([out_shape_value[1]],given_units+("²" if out_shape_value[0] == "area" else ""))}. Inscribed is a {in_shape} with unknown {in_shape_value[0]} of {write_paramaters([in_shape_value[1]],given_units+("²" if in_shape_value[0] == "area" else ""))}. The student must solve for the unknown {in_shape_value[0]} of {in_shape}, ask for this in a(n) {rd.choice(["direct","indirect"])} fashion. Use the answer choices {make_letter_choices(choices)}. {"If the inscribed shape is a rectangle, provide the fact that one side is half the length of its diagonal" if in_shape == 'rectangle' else ""}"

def shape_in_shape():
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

    correct = sp.ceiling(number_used)
    choices = rd.sample([correct,correct-1,sp.floor(1.2*correct),sp.ceiling(0.8*correct),sp.ceiling(2*correct)],k=5)
    given_units = rd.choice(["in","mm","cm","ft"])

    return f"You are creating the problems for a standardized math test. Write a(n) {rd.choice(["direct-concept", "application-based (Be creative with the scenario)", "real-life (Be creative with the scenario)"])} word problem that would be {rd.choice(["easy","moderately difficult","extremely difficult"])} for the average student. Provide a big shape of a(n) {big_shape} with a {shape_key[big_shape][1]} of {write_paramaters(big_parameters,given_units)}. Perseving {"volume" if use_3D else "area"}, it must be constructed out of smaller {small_shape}s with unknown {shape_key[small_shape][1]} of {write_paramaters(small_parameters,given_units)}. The student must solve for the unknown number of the smaller shape needed to make the big shape, ask for this in a(n) {rd.choice(["direct","indirect"])} fashion. Use the answer choices {make_letter_choices(choices)}."

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
            thirdSideBound = sp.sqrt(sides[0]**2 + sides[1]**2)
            if ansAngle == 'right':
                thirdSide = thirdSideBound
            elif ansAngle == 'obtuse': 
                thirdSideMaxBound = np.sum(sides)
                thirdSideMinBound = sp.ceiling(thirdSideBound.doit())
                thirdSide = rd.randrange(thirdSideMinBound,thirdSideMaxBound-1)
            else: 
                thirdSideMinBound = max(sides)
                thirdSideMaxBound = sp.floor(thirdSideBound.doit())
                thirdSide = rd.randrange(thirdSideMinBound+1,thirdSideMaxBound)
        else:
            leftover = 0 if largestIndex == 1 else 1
            thirdSideBound = sp.sqrt(sides[largestIndex]**2 - sides[leftover]**2)
            if ansAngle == 'right':
                thirdSide = thirdSideBound
            elif ansAngle == 'acute': 
                thirdSideMaxBound = max(sides)
                thirdSideMinBound = sp.ceiling(thirdSideBound.doit())
                thirdSide = rd.randrange(thirdSideMinBound,thirdSideMaxBound-1)
            else: 
                thirdSideMinBound = max(sides) - min(sides)
                thirdSideMaxBound = sp.floor(thirdSideBound.doit())
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