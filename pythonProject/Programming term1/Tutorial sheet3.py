#Question 1a
#a = float(input('enter a value for a = '))
#b = float(input('enter a value for b = '))
#c = float(input('enter a value for c = '))

#f = a * b - c
#print('the result is', f)


#Question 1b

#a = float(input('enter a value for a = '))
#b = float(input('enter a value for b = '))
#c = float(input('enter a value for c = '))

#x1 = ((b)+(b*b -4*a*c)**0.5)/(2*a)
#x2 = ((-b)-(b*b -4*a*c)**0.5)/(2*a)
#print('the result are', x1, x2)


#Question 2
#for x in range(101):
#    if x%5 ==0
#        print(x, end = ' ')


#Question 3
# list1 = list(range(30))
# even = 0
# for x in list1:
#     if x%2 == 0:
#         even += 1
# print(even)


Question 4
def hcf(a, b):
    HCF = 1
    for i in range(1, min(a, b), 1):
        if a%i == 0 and b%i == 0:
            HCF = i
    return HCF
print(hcf(24,32))


#Question 4b
# def string_test(s):
#     d = {"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#             d["UPPER_CASE"] += 1
#         elif c.islower():
#             d["LOWER_CASE"] += 1
#         else:
#             pass
#     return d
# print(string_test("The Brown Fox IS QUICK"))


# #Question 5a
# for i in range(1, 100, 1):
#     print(i, end = ' ')
#
# #Question 5b
# for i in range(100, 1, -1):
#     print(i)


#Question 5c
# for i in range(7, 77, 7):
#     print(i)

#Question 5d
# for i in range(20, 2, -2):
#     print(i)


#Question 6
# def calculate_the_sum(N):
#     if N<= 0:
#         return 'N must be a positive integer'
#     series_sum = 0
#     for i in range(1, N + 1):
#         series_sum += (1/i)
#     return series_sum
# print(calculate_the_sum(20))


#Question 7
# def times_table(A):
#     if A<= 0:
#         return 'A must be a positive integer'
#     results = []  #create an empty list to store the results
#     for i in range(1, 13):
#         product = A * i
#         results.append(product)
#     return results
# print(times_table(5))


#Question 7 other example
# def display_times_table(N):
#     if N <= 0:
#         print("N must be a positive integer.")
#         return
#
#     print(f"Multiplication Table for {N}:")
#
#     for i in range(1, 11):  # Display up to the 10 times table
#         product = N * i
#         print(f"{N} x {i} = {product}")
#
# # Input the value of N
# N = int(input("Enter a positive integer N: "))
#
# # Call the function to display the times table
# display_times_table(N)


#Question 8
# def divisor(N):
#     if N <= 0:
#         return 'N has to be a positive integer'
#     result = []
#     for i in range (1, N + 1):
#         if N%i == 0:
#             divisor = i
#             result.append(divisor)
#     return result
# print(divisor(20))


#Question 9
# def num(A):
#     if A <= 0:
#         return 'A must be a positive integer'
#     for i in range (1, A+1):
#         for a in range(1, i+1):
#             print(a, end = ' ')
#         print()
#     for i in range (A, 0, -1):
#         for a in range (1, i):
#             print(a, end = ' ')
#         print()
#
# print(num(5))

#Question 10



#Question 11
#Find the LCM of two positive intergers
# def lcm(a,b):
#     if a <= 0 and b <= 0:
#         return 'a and b must be positive intergers'
#     result = []
#     LCM = 1
#     for i in range(1, a*b+1):
#         if i%a == 0 and i%b == 0:
#             LCM = i
#             result.append(LCM)
#     return result[0]
# print(lcm(5,8))

#Question 11 other solution
# def lcm(a, b):
#     if a <= 0 or b <= 0:  # Check if either a or b is not positive
#         return 'a and b must be positive integers'
#
#     for i in range(1, a * b + 1):
#         if i % a == 0 and i % b == 0:
#             return i  # Return the LCM as soon as it's found
#
# print(lcm(4, 8))


# #Question 12
# def divisor(N):
#     if N <= 0:
#         return 'N has to be a positive integer'
#     result = []
#     total = 0
#     for i in range (1, N + 1):
#         if N%i == 0:
#             divisor = i
#             result.append(divisor)
#
#     for j in result:
#         total += int(j)
#
#     if total - N == N:
#         return 'perfect number'
#     return result
# print(divisor(28))

#Question 13
# def palindrome(number):
#     C = str(number)
#     reversed_C = C[::-1]
#     #The first colon : specifies the start of the slice. Since there's nothing before the first colon, it defaults to the beginning of the string.
#     #The second colon : specifies the end of the slice. Similarly, since there's nothing after the second colon, it defaults to the end of the string.
#     #-1 specifies the step. In this case, a step of -1 means that you want to traverse the string in reverse order, moving from the end towards the beginning.
#     if C == reversed_C:
#         return 'C is a palidrome'
#     else:
#         return number, 'is not a palindrome'
# print(palindrome(1671))

# def solution(A):
#     num_set = set(A)
#     for n in range(1, 1000000):
#         if n not in num_set:
#             return n
# print(solution([1,2,3]))

def solution(A, B, q):
    # Sentivity =  True positive / (True positive + False negatives)
    # Specificity = True negatuives / (True negatives + False posiitves)
    TP = sum([a==1 and b==1 for a, b, in zip(A,B)])
    TN = sum([a==0 and b==0 for a, b in zip(A,B)])
    FP = sum([a== and b==1 for a, b in zip(A,B)])
    FN = sum([a==1 and b==0 for a, b in zip(A,B)])

    if q: #will return specificity if q is true
        return TN/(TN + FP)
    else: #will return sensitivity is q is false
        return TP/(TP + FN)
print(solution([1,0,1,1,0,1], [0,1,1,0,0,1], True))