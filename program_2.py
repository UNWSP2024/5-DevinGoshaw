# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

#Name: Devin Goshaw
#date: 10/1/2025
#programm: math quiz program


import random

def check_answer(num1, num2, solution):
    answer=num1+num2
    if answer==solution:
        print('nice job you got the answer correct')
    else:
        print('you got the answer wrong the right answer is:', answer)

def quiz():
    num1=random.randint(0,99999)
    num2=random.randint(0,99999)
    print(num1)
    print('+', num2)
    print('-----')
    solution=float(input('answer: '))
    check_answer(num1, num2, solution)    
quiz()
