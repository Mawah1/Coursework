#Question 1
# def calculation(a, b):
#     addition = a + b
#     subtraction = a - b
#     return addition, subtraction
# print(calculation(10,4))

#Question2
# def absolute_value(a):
#     return a
# print(abs(absolute_value(-3.67)))

#Question 3
# def fizz_buzz(x):
#     if x%3==0 and x%5==0:
#         return 'Fizz Buzz'
#     elif x%5 == 0:
#         return 'Buzz'
#     elif x%3 == 0:
#         return 'Fizz'
#     else:
#         return x
# print(fizz_buzz(15))

#Question 4
# def multiples_3and5(limit):
#     multiple_list = []
#     for i in range(0,limit + 1):
#         if i%3==0 or i%5==0:
#             multiple_list.append(i)
#     return multiple_list
# print(multiples_3and5(20))

#Question 5
# def multiples_3and5(limit):
#     multiple_list = []
#     for i in range(0,limit + 1):
#         if i%3==0 or i%5==0:
#             multiple_list.append(i)
#     return sum(multiple_list)
# print(multiples_3and5(20))

#Question 6
# def check_prime(a):
#     if a<=1:
#         return 'false'
#     for i in range(2,int(a*0.5)+1):
#         if a%i == 0:
#             return 'false'
#         else:
#             return a,'is a prime number'
# print(check_prime())


# #Question 7
#def unique_elements(input_list):
#     #input_list = []
#     unique_list = []#set()
#     for i in input_list:
#         if i not in unique_list:
#             unique_list.append(i)
#     return unique_list

# def unique_elements(input_list):
#     unique_list = []
#     [unique_list.append(i) for i in input_list if i not in unique_list]
#     return unique_list
# print(unique_elements([1,2,3,3,3,3,4,5]))

# print(unique_elements([1,2,3,3,3,3,4,5]))
#
# def unique_elements2(input_list):
#     #input_list = []
#     unique_list = set(input_list)
#     return list(unique_list)
#
# print(unique_elements2([1,2,3,3,3,3,4,5]))

# #Question 8
# def calculate_L_U(sample_string):
# #    sample_string = str(a)
#     Lower = 0
#     Upper = 0
#     for char in sample_string:
#         if char.islower():
#             Lower+= 1
#         elif char.isupper():
#             Upper += 1
#     return Lower, Upper
# print(calculate_L_U('The quick Brown Fox'))

#Question 9




#Question 12
# a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11]
# for i in a:
#     if i%2 ==0:
#         print(i)

