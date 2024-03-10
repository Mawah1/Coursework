#Question 1
# Years = [1919, 1985, 1945, 2001, 2005, 2020]
# for i in Years:
#     print(2023 - i)


#Question 2; Given a list of intergers:
# list1 = [1, 24, 5, 17, 37, 23, 12, 16 , 8, 20, 11, 2, 35, 35]

# #Find all even numbers
# for i in list1:
#     if i%2 == 0:
#         print(i)

#Find largest number without using max()
# list1.sort()
# print(list1[-1])

#Find the second largest number
# print(list1[-2])

#Multiply all the items
# product = 1
# for i in list1:
#     product *= i
# print(product)

#Get unique values
# print(list1[1])

#Remove elements if multiplication of 3
# for i in list1:
#     if i%3 == 0:
#         list1.remove(i)
# print(list1)

#if element of list is between 30 and 45, make it 1 else 0
# for i in list1:
#     if 30<i<45:
#        list1.index(i)
#        list1[list1.index(i)] = 1
#     else:
#          list1[list1.index(i)] = 0
# print(list1)

#other way to sole above question
# for i in list1:
#     for index, i in enumerate(list1):
#         if 30 < i < 45:
#             list1[index] = 1
#         else:
#             list1[index] = 0
#     break
# print(list1)

#Question 3
# list2 = [2, 4, 28, 17, 6, 9, 12, 18]
# list3 = [2, 13, 17, 19, 18, 24, 6, 23]
# element_to_check = 0
# for element_to_check in list2:
#     if element_to_check in list3:
#         print(element_to_check, "is an element of list2 and list3")
#     else:
#         print(element_to_check, 'is not an element of list 3')
#
# print(element_to_check)

#Question 4
# example_string = 'Hello, my telephone number if 07446741541'
# extracted_digits = ' '
#
# for char in example_string:
#     if char.isdigit():
#         extracted_digits += char
# print('the extracted digits are', extracted_digits)

#Question 5
# string1 = 'onomatopoeia'
# string2 = 'metaphor'
# string3 = 'is'
# string4 = 'on'
# string5 = 'a'
# string6 = 'similie'
# string7 = '1'
# string8 = '3'
# string9 = 'tablet'
# string10 = 'liverpool'
# char = ' '
# total = 0
# for char in string1, string2, string3, string4, string5, string6, string7, string8, string9 and string10:
#     char += 1
#     total = char
#     if total >= 2

