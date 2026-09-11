#1

for i in range(1,6):
    print("hello")

#2

for num in range(0,10):
    print(num,end=" ")

#3

for num1 in range(1,11):
    print(num1,end=" ")

#4

for num2 in range(10,0,-1):
    print(num2,end=" ")

#5

for num3 in range(5,50,5):
    print(num3,end=" ")

#6

for num4 in range(2,20):
    if num4%2==0:
        print(num4,end=" ")
   
#7

for num5 in range(1,20):
    if num4%2==1:
        print(num5,end=" ")

#8

for num6 in range(1,20):
    if num6%3==0:
        print(num6,end=" ")    

#9

for num7 in range(20,0,-2):
    print(num7,end=" ")

#10
n=int(input("enter a number : "))
for k in range(1,n+1):
    print(k,end=" ")

#11

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

#12

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)

#13

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)

#14

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)

#15

n = int(input("Enter n: "))
count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        count = count + 1
        print("Even numbers:", count)


#16

n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total = total + i
    print("Sum:", total)


#17

n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total = total + i
        print("Sum of even numbers:", total)

#18

n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        total = total + i
        print("Sum of odd numbers:", total)

#19

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#20

n = int(input("Enter n: "))
result = 1

for i in range(1, n + 1):
    result = result * i
    print("Result:", result)

#21

text = input("Enter a string: ")

for ch in text:
    print(ch)

#22
text = input("Enter a string: ")

for ch in text:
    print(ch, end="")

#23

text = input("Enter a string: ")
count = 0

for ch in text:
    count = count + 1
    print("Number of characters:", count)

#24

text = input("Enter a string: ")
count = 0

for ch in text:
    if ch == "a":
        count = count + 1
        print("Number of a:", count)

#25

text = input("Enter a string: ")
count = 0

for ch in text:
    if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        count = count + 1
        print("Uppercase letters:", count)

#26

for i in range(3):
    for j in range(4):
        print("*", end="")
    print()

#27

for i in range(4):
    for j in range(5):
        print("*", end="")
    print()

#28

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

#29

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#30

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()