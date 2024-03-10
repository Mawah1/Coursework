#Question 1
import math #import maths for the value of pi.
#Here, we know that a real number consist of both positive and negative irrational and rational numbers.
#Write a function
#Write the code (including the formular) for the numerator and denominator of the equation

def solve_equation(x):
    numerator = (2 * math.pi) * ((x**x) - (3*x))
    denominator = ((x**x)-1)
#We need to identify areas where the equation is unsolvable.
#Here, we know that a number cannot be divided by zero.
#We identify possible values of x that the user may input that will result in the denominator being equal to zero.
#Create an If function that eliminates python having to solve the equation when the denominator is zero.
    if denominator == 0:
        print('solution is unsolvable as one cannot divide by zero')
        return 'None'
    else: #Then create an alternative of the If function that solves the equation when the denominator is not equal to zero.
        solution = numerator/denominator
        return solution
#test python program
print(solve_equation(4)) #test for when the equation is solvable
print(solve_equation(1)) #test for when the equation is not solvable



#Question 2a
def countDigits(a): #create a function
    #convert the value (a) to an absolute value such that it eliminates the negative sign(when counting) when the user inputs a negative number.
    #'abs' returns the absolute value meaning it returns only positive values
    #convert that absolute value into a string and find the length of the string using 'len'
    counts = len(str(abs(a)))
    return counts
#test the code
print(countDigits(-3545)) #test for when the integer entered is a negative
print(countDigits(456))  #test for when the interger entered is positive



#Question 2b
#import 'random' to load the random module containing a number of random number generation-related functions
import random
#create a random function
def generating_random():
#set the range for the a and b values as defined in the question using 'randint'
    a = random.randint(10,9999)
    b = random.randint(10,9999)
#create a function within random function that returns True and prints the following below when 'a' has more or equal digits to 'b'
# and returns False and prints the following when 'a' has fewer digits than 'b'
    if len(str(a))==len(str(b)):
        print(a, 'has equal digits to', b)
    elif len(str(a))>len(str(b)):
        print(a, 'has more digits than', b)
    else:
        print(a, 'has fewer digits than', b)
#test the python program
generating_random()



#Question 3a
#create a dictionary that contains student_id, student name, and the list of modules they study (also including the module_id, module title and marks)

students = dict(s001={'name': 'Alice Smith', 'modules': {'m101': {'title': 'Introduction to Mathematics', 'marks': 92},
                                                    'm102': {'title': 'Fundamentals of Physics', 'marks': 88}}},
        s002={'name': 'Bob Johnson', 'modules': {'m101': {'title': 'Introduction to Mathematics', 'marks': 75},
                                                  'm102': {'title': 'Fundamentals of Physics', 'marks': 85}}})


#Question 3b
#Create a function defining its paramemters/variables as student_id, module_id and module_info. This will allow the user to be able to
#target a key student and add the new module they are taking (including the module information)
def addModule(student_id, module_id, module_info):
    if student_id in students: #iterate student_id within the students dictionary
        if 'modules' in students[student_id]:  #iterate only the module dictionary within student_id specified in students
            students[student_id]['modules'][module_id] = module_info   #add the module information within the module dictionary making sure to include its module_id
            return students   #return the new student dictionary including the new added module
    else: #take into account when the user tries to include a module to a student_id that does not exist within the dictionary
        print(student_id, 'is not in the list of students')
#test the python program
print(addModule('s001','m103', {'title': 'Advanced mathematics', 'marks': 94}))  #test for when the student is listed in the dictionary
print(addModule('s003','m103', {'title': 'Advanced mathematics', 'marks': 94}))   #test for when the student is not listed in the dictionary


#Create a function defining its paramemters/variables as student_id and module_id. This will allow the user to be able to
#target a key student and remove a module they are taking (including the module information)
def removeModule(student_id, module_id):
    if student_id in students:
        if 'modules' in students[student_id]:
            del students[student_id]['modules'][module_id] #use the 'del' element in python to delete the module you intend to delete
            return students #return the new dictionary of students
    else: #take into account when the user tries to include a module to a student_id that does not exist within the dictionary
        print(student_id, 'is not in the list of students')
#test the python program
print(removeModule('s001','m102')) #test for when the student is listed in the dictionary
print(removeModule('s003','m102'))  #test for when the student is not listed in the dictionary



#Question 3c
def view_profile(student_id): #create a function defining the variable/parameters as student_id
    for student_key, student_info in students.items():  #iterate the students dictionary
        if student_key == student_id: #if the student_key in the dictionary is equal to the student_id inputed by the user then return the student information
            return student_info
        else: #if the student_id is not equal to the student_key then that means the student is not listed in the dictionary
            return student_id, 'is not listed'
print(view_profile('s001'))  #test for when the student is listed in the dictionary
print(view_profile('s003'))   #test for when the student is not listed in the dictionary


#Question 3d
#Initialise the variables (highest and lowest average) to zero that will store the students' marks.
highest_avg = 0
lowest_avg = 0
#Initialise the variables (highest and lowest student) to none that will store the students' names.
highest_student = None
lowest_student = None
list_of_avg = [] #create an empty list to store students' average marks
#this list will be used to calculate the maximum and minimum average marks
for student_id, student_info in students.items(): #iterate the students dictionary
#Inside this outer loop, initialise the variables (total_marks and module_count) to zero.
#These variables will be used to calculate the students average marks
    total_marks = 0
    module_count = 0
    for modules in student_info['modules'].values(): #iterate over the modules of each student
        total_marks += modules['marks']   #calculate the total marks by summing up the module marks
        module_count += 1    #increment/count the module for each student
        avg_marks = total_marks/module_count
    list_of_avg.append(avg_marks) #append/add the average marks into the list
    max_avg = max(list_of_avg) #calculate the maximum average mark
    min_avg = min(list_of_avg) #calculate the minimum average mark
    if avg_marks == max_avg:
        highest_student = student_info['name'] #if the current student's average marks equal to the max average, assign their name to the highest student variable
    elif avg_marks == min_avg:
        lowest_student = student_info['name'] #if the current student's average marks equal to the max average, assign their name to the highest student variable

#Test the python program
print(lowest_student, 'has the lowest average score of', min_avg)
print(highest_student, 'has the highest average score of', max_avg)



#Question 3e
#Initialise the variables (highest and lowest average) to zero that will store the students' marks.
highest_avg = 0
lowest_avg = 0
#Initialise the variables (highest and lowest student) to none that will store the students' names.
highest_student = None
lowest_student = None
list_of_avg = []  #create an empty list to store students' average marks
for student_id, student_info in students.items():  #iterate the students dictionary
#Inside this outer loop, initialise the variables (total_marks and module_count) to zero.
#These variables will be used to calculate the students average marks
    total_marks = 0
    module_count = 0
    for modules in student_info['modules'].values(): #iterate over the modules of each student
        total_marks += modules['marks']   #calculate the total marks by summing up the module marks
        module_count += 1  #increment/count the module for each student
        avg_marks = total_marks/module_count  #calculate the average marks
    list_of_avg.append((avg_marks,student_info))  #append each students' average mark and student information into the empty list
    list_of_avg.sort()  #sort the empty list from the student with the lowest average to highest
print(list_of_avg)