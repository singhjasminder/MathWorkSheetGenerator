import datetime

def MultiplicationProblemCreator(input_list):
    print("Creating Multiplication Worksheet.......")
    print ('\n')
    date_timestamp = str(datetime.date.today())
    file_name = "Multiplication_Worksheet_" + date_timestamp + (".txt")
    createFile = open(file_name,"w+")
    num_questions = int((len(input_list)/2))
    index = 0

    for _ in range(num_questions):
        question = str(input_list[index]) + " X " + str(input_list[index+1]) + " = " + '\n'
        createFile.write(question)
        index = index+2

    print ("Worksheet Created!!")