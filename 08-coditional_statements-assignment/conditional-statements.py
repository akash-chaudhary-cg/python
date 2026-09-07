#1

a=10
if a>10:
    print("a is greater than 10")

#2
age=20
if age>=18:
    print("You are eligible to vote")

#3
b=int(input("Enter your number:"))
if b > 0:
    print("You have entered a positive number")

#4
c=int(input("Enter your marks:"))
if c >= 40:
    print("You have passed the exam")
else:
    print("You have failed the exam")

#5
d=int(input("Enter your number:"))
if d == 0:
    print("You have entered zero")

#6
e=int(input("Enter your number:"))
if e > 0:
    print("You have entered a positive number")
else:
    print("You have entered a negative number")

#7
age1=int(input("Enter your age:"))
if age1 >= 18:
    print("adult")
else:
    print("minor")

#8
a1=int(input("Enter a number: "))
if a1 % 2 == 0:
    print("your number is Even")
else:
    print("your number is Odd")

#9
marks1=int(input("Enter your marks: "))
if marks1 >= 40:
    print("You have passed the exam")
else:
    print("You have failed the exam")

#11
marks2=int(input("Enter your marks: "))
if marks2 >= 90:
    print("You have got A grade")   
elif marks2 >=75:
        print("You have got b grade")  
elif marks2 >=60:
        print("You have got c grade") 
elif marks2 >=40:
        print("You have got d grade")
else:
    print("you are fail in exam")  

#12

num=input("input your number")
if num > 0:
    print("your number is positive")
elif num == 0:
    print("your number is zero")
else:
    print("your number is negetive")

#13

num1=input("choose your number(1,2,3,4,5)")
if num1 == 1:
    print("you choose monday")
elif num1 == 2:
    print("you choose tuesday")
elif num1 == 3:
    print("you choose wedneaday")
elif num1 == 4:
    print("you choose thursday")
elif num1 == 5:
    print("you choose friay")

#14

marks3=int(input("enter your marks"))

if marks3 > 90:
    print("excellent")
elif marks3 > 75:
    print("good")
elif marks3 > 33:
    print("pass")
else:
    print("fail")

#15

num2=int(input("input your number"))
if num2 == 1:
   print("number is 1")
elif num2 == 2:
    print("number is 2")
elif num2 == 3:
    print("number is 3")
else:
    print("other")

#16

a2 = int(input("Enter the age: "))
if a2 >= 18:
    if a2 <= 60:
        print("Between 18 and 60")


#17

marks4=int(input("your marks"))
if marks4 >= 40:
    print("PASS")
elif marks4 >= 75:
    print("good")
else:
    print("failed")

#18

marks5=int(input("Enter a number : "))
if marks5>0 :
    if marks5>100 :
        print("given number is greter than 100")
else:
    print("given number is negative")        

#19

age2=int(input("Enter Your age : "))
if age2>=18 :
    if age2<=60 :
        print("Your age is between 18 and 60.")
else:
    print("your age is eigher greter than 60 or lessthan 18.")

#20

num3=int(input("Enter a number : "))
if num3!=0 :
    if num3>0 :
        print("given number is positive")
    elif num<0 :
        print("given number is negative")    
else:
    print("given number is zero")      

#21

age3=int(input("Enter Your age : "))
marks6=int(input("Enter Your marks : "))
if age3>=18 and marks6>=40 : 
    print("Your are Eligible for Higher study ")
else:
    print("You are'nt eligible for higher study !!!\n better luck next time!!")    

#22

num4=int(input("enter a number : "))
if num4>10 and num4<100 : 
    print("Your number is special !!")
else:
    print("Your number is normal")

#23

age4=int(input("Enter Your age : "))
has_id=True
if age4>=18 and has_id==True: 
    print("Allowed to give exam")
else:
    print("Your are not allowed for giving exam!!")

#24

first_number=int(input("Enter first number :"))
second_number=int(input("Enter second number :"))
if first_number>10 and second_number>10 :
    print("both number are greter than 10")
else:
    print("both number are lessthan 10")

#25

num5=int(input("Enter first num : "))
if num5<0 or num5>100 :
    print("given num is either less than 0 or greater than 100")
else:
    print("given num is between 0 to 100")

#26

is_closed=False
if not is_closed :
    print("open door")
else:
    print("closed door")    

#27

num6=int(input("Enter a number:"))
if num6>10 and num6<50 :
    print("taken number id between 10 and 50.")
else:
    print("taken number is not between 10 and 50.")


#28

if num7 >10 or num<50:
    print("it is outside of range")

#29

is_student=bool(input("youe are student"))
has_id1=bool(input("you have id"))
has_ticket=bool(input("you have ticket"))
if is_student == True:
    if has_id1 == True:
        if has_ticket == True:
            print("allowed")

#30

age5=int(input("enter your age"))
mark=int(input("enter your mark"))
has_id2=bool(input("you have id??"))
if age5 >= 18 and mark >= 40 and has_id2 is True:
    print("eligible")
else:
    print("not eligible")
