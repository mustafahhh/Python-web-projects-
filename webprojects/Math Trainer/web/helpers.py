import random

#Two levels 
def EA(level):
    

    #level 1 

    if level == 1 :
        range1 = 1
        range2 = 20 
        #Generate number between range1 and range2  
        operator = random.choice(['*','-','+','/'])
        operator2 = random.choice(['*','-','+','/',' ' ,' ',' ']) #We made ' ' so we make the chance of having equation that has 2 operators less
        numbers=[random.randint(range1,range2),random.randint(range1,range2),random.randint(range1,range2)]
        if operator2 != ' ':
            result = eval(f"{numbers[0]} {operator} {numbers[1]} {operator2} {numbers[2]}") #The equation Answer
            while result % 1 != 0 or result < 0:#Here we are applying our rules for the equation answer 
                #We dont want the number be like -1 or 0.32154
                numbers=[random.randint(range1,range2),random.randint(range1,range2),random.randint(range1,range2)]
                result = eval(f"{numbers[0]} {operator} {numbers[1]} {operator2} {numbers[2]}")#The equation Answer

            return f"{numbers[0]} {operator} {numbers[1]} {operator2} {numbers[2]}"
        else:
            result = eval(f"{numbers[0]} {operator} {numbers[1]} ")
            while result % 1 != 0 or result < 0:#Here we are applying our rules for the equation answer 
                #We dont want the number be like -1 or 0.32154
                numbers=[random.randint(range1,range2),random.randint(range1,range2),random.randint(range1,range2)]
                result = eval(f"{numbers[0]} {operator} {numbers[1]}")
            return f"{numbers[0]} {operator} {numbers[1]} "

    #Level 2 

    if level == 2 :
        range1 = 3
        range2 = 30
        #Generate number between range1 and range2  
        operator = random.choice(['*','-','+','/'])
        operator2 = random.choice(['*','-','+','/',' ' ,' ',' '])#We made ' ' so we make the chance of having equation that has 2 operators less
        numbers=[random.randint(range1,range2),random.randint(range1,range2),random.randint(range1,range2)]
        if operator2 != ' ':
            result = eval(f"{numbers[0]} {operator} {numbers[1]} {operator2} {numbers[2]}")
            while result % 1 != 0 or result < 0:#Here we are applying our rules for the equation answer 
                #We don't want the number be like -1 or 0.32154
                numbers=[random.randint(range1,range2),random.randint(range1,range2),random.randint(range1,range2)]
                result = eval(f"{numbers[0]} {operator} {numbers[1]} {operator2} {numbers[2]}")

            return f"{numbers[0]} {operator} {numbers[1]} {operator2} {numbers[2]}"
        else:
            result = eval(f"{numbers[0]} {operator} {numbers[1]} ")
            while result % 1 != 0 or result < 0:#Here we are applying our rules for the equation answer 
                #We dont want the number be like -1 or 0.32154
                numbers=[random.randint(range1,range2),random.randint(range1,range2),random.randint(range1,range2)]
                result = eval(f"{numbers[0]} {operator} {numbers[1]} ")
            return f"{numbers[0]} {operator} {numbers[1]} "