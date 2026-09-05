#task 1
name=input("Enter Your Name: ")
print(f"Hello {name} \n welcome to python language")

#task 2
city=input("Enter Your City: ")
print(f"Your city is {city}")

#task 3
a,b=input("Enter Your Name and Enter Your Age: ").split()
print(f"Your name is {a} and your age is {b}")

#task 4
a=input("")
print(type(a))

#task 5
a=int(input("Enter Your Age: "))
print(type(a))

#task 6
a,b=input("Enter Your first Name and Enter Your last name: ").split()
print(f"Your first name is {a} and your last name is {b}")

#task 7
a,b,c=input("Enter Your name and Enter your city and Enter your collage name: ").split()
print(f"Your name is {a} and your city is {b} and your collage name is {c}")

#task 8
a,b="enter your first name and enter your last name: ".split()
print(f"hello {a} {b}")

#task 9
a,b=input("enter python programming: ").split()
print(f"python programming:  {a} and {b}")

#task 10
a,b,c=input("Enter three words separated by spaces: ").split()
print(f"Your first word is {a}, your second word is {b}, and your third word is {c}.")

#task 11
a="25"
print(type(int(a)))

#task 12
a="25.5"
print(type(float(a)))

#task 13
a=100
print(type(str(a)))

#task 14
a=int(input("Enter Your Age: "))
print(type(str(a)))

#task 15
a=12.5
print(type(str(a)))

#task 17
a,b=input("Enter age of maturity and enter minimum age of voter: ").split()
print(f"Age of maturity is {a} and minimum age of voter is {b}")

#task 18
name = "Rahul"
age = 20
print(f"My name is {name} and I am {age} years old.")

#task 19
a=10
b=20
print(f"The sum of {a} and {b} is {a+b}.")

#task 20
a,b=input("enter your name and age: ").split()
print(f" user's name is {a} and user's age is {int(b)}")

#task 21
price_of_product=99.98888
print(f"the price of product is {price_of_product:.2f}")

#task 22
print(".2f is using for 2 decimal floting number and round off the number after 2 decimal point")

#task 23
a,b,c=input("Enter product name and it's price and also enter it's quantity: ").split()
print(f"product name is {a} and it's price is {float(b):.2f} and it's quantity is {int(c)}")

#task 24
print("A", "B", "C")

#task 25
print("2026", "08", "19")

#task 26
print("hello",end="")
print("world!!")

#task 27
a,b=map(int,input("Enter first number and enter second number: ").split())
print(f"The sum of {a} and {b} is {a+b}.")

#task 28
price,quantity=map(int,input("Enter price and enter quantity: ").split())
print(f"Total price is {float(price)*quantity}.")

#task 29
name,age,marks=map(str,input("Enter your name and age and marks: ").split())
print(f"Your name is {name} and your age is {int(age)} and your marks is {int(marks)}.")

#task 30
name,age,height,city=map(str,input("Enter your name and age and height and city: ").split())
print(f" your name is {name} and your age is {int(age)} and your height is {float(height)} and your city is {city}")