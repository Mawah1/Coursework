
print("******")
print("*    *")
print("*    *")
print("*    *")
print("*    *")
print("******")

a = 9
b = 2
print(a//b)
print(a%b)

e = 3
f = 5
e,f = f,e
print(e)
print(f)

mass = 73
height = 1.65
bmi = mass/(height**2)
print(bmi)

radius = 5
Pi = 3.14
Circumference = 2*Pi*radius
Area = Pi*radius*radius
print(Circumference)
print(Area)

a = 5
b = 7
c = 3
Circumference = a+b+c
p = Circumference/2
Area = (p*(p-a)*(p-b)*(p-c))**(1/2)
print(Circumference)
print(Area)

num_boxes = 41
Camel = 6
Mule = 4
Donkey = 2
C = num_boxes//Camel
M = (num_boxes%Camel)//4
D = 41 - ((6*C) + (4*M))
print(str(C)+" Camels")
print(str(M)+" Mules")
print(str(D)+" Donkey")


#further practice
x = 4.75
print(type(x))

y = 5
print(type(y))

print(int(x))
print(float(x))
