import random
from AdditionWorkSheet import AdditionProblemCreator
from MultiplicationWorkSheet import MultiplicationProblemCreator

def WorksheetFunction(functionType):
    value_list = []

    try:
        number_of_problems = int(input("How many questions? "))
        lower_limit = int(input("Please enter starting value: "))
        upper_limit = int(input("Please enter ending value: "))

    except ValueError:
        print("Please enter valid integer value")
        return
    
    for _ in range(number_of_problems*2):
        value_list.append(random.randint(lower_limit,upper_limit))

    #print(len(value_list))
    #print(value_list)

    if (functionType == 1):
        AdditionProblemCreator(value_list)
    else:
        MultiplicationProblemCreator(value_list)
