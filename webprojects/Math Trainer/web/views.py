from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
import json
from django.http import HttpResponse
from .helpers import EA
import random
from django.views.decorators.csrf import csrf_exempt

#View
def main(request):
    return render(request,'main.html')

def quiz(request):
    return render(request,'quiz.html')

def answers(request,Answerss):
    return render (request,'Answers.html',{'Answered' : Answerss})

def stats(request):
    return render(request,'stats.html')

def charts(request):
    return render(request,'charts.html')

def AnswersChart(request): 
    return render(request,'AnswersChart.html')

def ResultsChart(request):
    return render(request,'ResultChart.html')

#API
@csrf_exempt 
def generateequation(request,level):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8').replace("'", '"'))
        level = data["Level"]
    if level == 1 :
        range1 = 1
        range2 = 20 
        #Generate number between range1 and range2  
        operator = random.choice(['*','-','+','/'])
        operator2 = random.choice(['*','-','+','/',' ',' ']) #We made ' ' so we make the chance of having equation that has 2 operators less
        numbers=[random.randint(range1,range2),random.randint(range1,range2),random.randint(range1,range2)]
        if operator2 != ' ':
            result = eval(f"{numbers[0]} {operator} {numbers[1]} {operator2} {numbers[2]}") #The equation Answer
            while result % 1 != 0 or result < 0:#Here we are applying our rules for the equation answer 
                #We dont want the number be like -1 or 0.32154
                numbers=[random.randint(range1,range2),random.randint(range1,range2),random.randint(range1,range2)]
                result = eval(f"{numbers[0]} {operator} {numbers[1]} {operator2} {numbers[2]}")#The equation Answer

            Response = '{"Equation" :' +  f'"{numbers[0]} {operator} {numbers[1]} {operator2} {numbers[2]} "' + '}'
            return HttpResponse(Response)
        else:
            result = eval(f"{numbers[0]} {operator} {numbers[1]} ")
            while result % 1 != 0 or result < 0:#Here we are applying our rules for the equation answer 
                #We dont want the number be like -1 or 0.32154
                numbers=[random.randint(range1,range2),random.randint(range1,range2),random.randint(range1,range2)]
                result = eval(f"{numbers[0]} {operator} {numbers[1]}")
            Response = '{"Equation" :' +  f'"{numbers[0]} {operator} {numbers[1]} "' + '}'

            return HttpResponse(Response)

    #Level 2 

    if level == 2 :
        range1 = 3
        range2 = 30
        #Generate number between range1 and range2  
        operator = random.choice(['*','-','+','/'])
        operator2 = random.choice(['*','-','+','/',' ' ,' ',' '])#We made ' ' so we make the chance of having equation that has 2 operators less
        brackets = random.choice(["("," ", " "])
        if brackets == "(": brackets2 = ")"
        numbers=[random.randint(range1,range2),random.randint(range1,range2),random.randint(range1,range2)]
        if operator2 == ' ':
            result = eval(f"{numbers[0]} {operator} {numbers[1]} {operator2} {numbers[2]}")
            while result % 1 != 0 or result < 0:#Here we are applying our rules for the equation answer 
                #We don't want the number be like -1 or 0.32154
                numbers=[random.randint(range1,range2),random.randint(range1,range2),random.randint(range1,range2)]
                result = eval(f"{brackets}{numbers[0]} {operator} {numbers[1]}{brackets2} {operator2} {numbers[2]}")
            Response = '{"Equation" :' +  f'"{numbers[0]} {operator} {numbers[1]} {operator2} {numbers[2]}"' + '}'
            return HttpResponse(Response)
        else:
            result = eval(f"{numbers[0]} {operator} {numbers[1]} ")
            while result % 1 != 0 or result < 0:#Here we are applying our rules for the equation answer 
                #We dont want the number be like -1 or 0.32154
                numbers=[random.randint(range1,range2),random.randint(range1,range2),random.randint(range1,range2)]
                result = eval(f"{numbers[0]} {operator} {numbers[1]} ")
            Response = '{"Equation" :' +  f'"{numbers[0]} {operator} {numbers[1]} "' + '}'
            return HttpResponse(Response)



@csrf_exempt
def CheckAnswers(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8').replace("'", '"'))
        Answers = data["Answers"].split(',')
        Equations = data["Equations"].split(',')
        Checker = []
        RightAnswers = 0 
        #1 means Right
        #0 means Wrong
        Index = 0 
        print(Equations,Answers)
        for i in Equations:
            if int(eval(i)) == int(Answers[Index]):
                Checker.append(1)
                print(i,Answers,Index)
                RightAnswers = RightAnswers + 1
            else: 
                Checker.append(0)
            Index = Index + 1 
        return HttpResponse('{"Answered" :' + f'"{RightAnswers}"' + " } ")
    else:
        return HttpResponse("Can not use 'GET' method on this")
            

