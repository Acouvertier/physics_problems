import random as rd
import numpy as np

class PhysicsProblems:
    CONSTANTS = {
        "K": 9e9,
        "e0": 8.85e-12,
        "qe": -1.6e-19,
        "me": 9.11e-31,
        "n": 1e-9,
        "mu": 1e-6,
        "m": 1e-3,
        "p": 1e-12,
        "c": 1e-2
        }

    def __init__(self):
        pass

    #Electricity and Magnetism
    def charge_conservation(num_balls: int):
        
        if num_balls < 2:
            print("Must use at least two balls")
            return None
        
        isEven = rd.choice([True,False])
        if isEven:
            holder = rd.sample(range(-6,6,2),k=2)

        else: 
            holder = rd.sample(range(-5,5,2),k=2)


            
        for _ in range(num_balls - 2):
            isEven = not isEven
            if isEven:
                holder.append(rd.randrange(-6,6,2))
            else: 
                holder.append(rd.randrange(-5,5,2))

        ans = (holder[0] + holder[1])/2
        for i in range(2, num_balls):
            ans = (ans + holder[i])/2
        
        print(f"You are given {num_balls} metal balls that are placed in a line from left to right.\nThe charges on these balls, from left to right, are given as {holder},\nwhere the the first number is the leftmost ball and the last is the rightmost.\nIf the balls are made touch, one pair at a time from left to right, what will the net charge on the last ball be?\n(Ex. If there are 3 balls, the leftmost will touch the middle, then the middle will touch the rightmost).\nANSWER: {ans}")

    def electric_force_2D_n_particles_solver(charges: list, positions: list, forceOn: int):
        k = PhysicsProblems.CONSTANTS["K"]
        positionArrays = [np.array(i) for i in positions]
        fixedEnd = positionArrays[forceOn-1]
        fixedCharge = charges[::].pop(forceOn-1)
        positionArrays.pop(forceOn-1)
        rVecs = [fixedEnd - i for i in positionArrays]
        netForce = np.array([0,0])
        for particle in range(len(rVecs)):
            currentR = rVecs[particle]
            r3 = np.sqrt(currentR.dot(currentR))**3
            force = ((k*fixedCharge*(charges[particle]))/(r3))*currentR
            netForce = netForce + force
            
        return [f"The net force on the {fixedCharge}C charge at the position ({fixedEnd[0]}m,{fixedEnd[1]}m) is:\n({netForce[0]})i + ({netForce[1]})j N", netForce]

    def electric_force_1D_two_particles_question():
        k = PhysicsProblems.CONSTANTS["K"]
        
        isHorizontal = rd.choice([True,False])
        particle_to_find = rd.choice([1,2])
        particle_number = "1st" if particle_to_find == 1 else "2nd"
        
        if isHorizontal:
            fixedY = [0,0]
            fixedX = rd.sample(range(-10,10,1),k=2)
            if fixedX[0] > fixedX[1]:
                orientation = "to the right of"
            else: 
                orientation = "to the left of"
            distance = abs(fixedX[0]-fixedX[1])
            vectorIndex = 0
        else: 
            fixedX = [0,0]
            fixedY = rd.sample(range(-10,10,1),k=2)
            if fixedY[0] > fixedY[1]:
                orientation = "above"
            else: 
                orientation = "below"
            distance = abs(fixedY[0]-fixedY[1])
            vectorIndex = 1

        chargeScale = rd.choice(["n","mu","m","p"])
        chargeMultiple= PhysicsProblems.CONSTANTS[chargeScale]
        distanceScale = rd.choice(["m","c"])
        distanceMultiple = PhysicsProblems.CONSTANTS[distanceScale]
        
        positionArrays = list(map(lambda x,y: [x*distanceMultiple,y*distanceMultiple], fixedX, fixedY))
        chargeArray = [rd.randrange(-7,7,2)*chargeMultiple for _ in range(2)]
        
        forceVec = PhysicsProblems.electric_force_2D_n_particles_solver(chargeArray, positionArrays, particle_to_find)[1][vectorIndex]
        
        direction = "attractive" if chargeArray[0]*chargeArray[1] < 0 else "repulsive"
        phrases = [f"a charge of {chargeArray[0]/chargeMultiple}{chargeScale}C", f"a charge of {chargeArray[1]/chargeMultiple}{chargeScale}C", f"a distance of {distance}{distanceScale}m", f"{abs(forceVec)}N"]
        unknownPhrases = ["an unknown charge", "an unknown charge","an unknown distance", "unknown strength"]
        missing = ["What is the missing charge?", "What is the missing charge?", "What is the distance between the charges?", f"What is the force on the {particle_number} particle?"]
        ans = [chargeArray[0],chargeArray[1],distance,forceVec]
        units = ["C","C","m","N"]
        quantityToFind = rd.choice([1,2,3])
        phrases[quantityToFind] = unknownPhrases[quantityToFind]

        

        return f"You are given two charges, one has {phrases[0]} and the other has {phrases[1]}.\nThey are situated such that the first charge is {phrases[2]} {orientation} the second charge\nand they experience a force of {phrases[3]} that is {direction}. {missing[quantityToFind]}\nANSWER: {ans[quantityToFind]}{units[quantityToFind]}"

    def electric_force_2D_n_particles_question(num_particles:int):
        if num_particles < 2:
            print("Must have at least 2 particles for force problem")
            return None
        
        k = PhysicsProblems.CONSTANTS["K"]
        
        unitDistances = range(-5,5,1)
        fixedX = rd.sample(unitDistances,k=num_particles)
        fixedY = rd.sample(unitDistances,k=num_particles)

        chargeScale = rd.choice(["n","mu","m","p"])
        chargeMultiple= PhysicsProblems.CONSTANTS[chargeScale]
        distanceScale = rd.choice(["m","c"])
        distanceMultiple = PhysicsProblems.CONSTANTS[distanceScale]
        
        positionArrays = list(map(lambda x,y: [x*distanceMultiple,y*distanceMultiple], fixedX, fixedY))
        chargeArray = [rd.randrange(-7,7,2)*chargeMultiple for _ in range(num_particles)]
        particle_to_find = rd.choice(range(1,num_particles+1))
       
        ans = PhysicsProblems.electric_force_2D_n_particles_solver(chargeArray, positionArrays, particle_to_find)
        
        particlePhrase = ""
       
        for i in range(num_particles):
            particlePhrase = particlePhrase + f"charge {i+1} of {(chargeArray[i])/chargeMultiple}{chargeScale}C at location ({(positionArrays[i][0])/distanceMultiple}{distanceScale}m,{(positionArrays[i][1])/distanceMultiple}{distanceScale}m)\n"

        return "You are given the following charges at fixed positions:\n" + particlePhrase + f"What is the net electric force on charge {particle_to_find}?\nAnswer: {ans[0]}"

print(PhysicsProblems.electric_force_2D_n_particles_question(2))

            