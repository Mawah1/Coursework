#even = [0,2,4,6,8,10,12,14,16,18,20]
#for n in even:
#    print(n,end = ' ')

x = 0
while x<=20:
      print(x, end = ' ')
      x += 1


range(30)
print(list(range(0,30,2)))

range(2,7)
print(list(range(3,7)))

for n in range (10):
    print(2**n, end = ' ')


for x in range(20):
    if x%2 == 0:
        print (x, end = ' ')
    else:
        print('odd', end = ' ')


number = 1
while number < 200:
    print(number)
    number = number * 2
