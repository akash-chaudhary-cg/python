# Practice problem

# Q=1

def a():
    city="Tharad"
    print(city)
a()

# [-----------------------------------------------------]

# Q-2
school="Coding-Gita"
def call():
    global school
    print(school)
call()

# [-----------------------------------------------------]

# Q-3
num=10
if num > 0:
    word="Hello"
print(word)

# [-----------------------------------------------------]

# Q-4

for i in range(0,2):
    print(i)
    
print(i)

# [-----------------------------------------------------]

# Q-5

Difference = "where does we can access variable it's called scope and how much time we can use varible it's called lifetime ."

# [-----------------------------------------------------]

# Q-6

test=200
value=100

# [-----------------------------------------------------]

# Q-7

clicks = 0
def click():
    global clicks
    clicks += 1
    print(clicks)
click()

# [-----------------------------------------------------]
# Q-8
ans="because in function we print name before decleare and also not we do not call globle scope" 

# [-----------------------------------------------------]

# Q-9

def a():
    num=10
    def b():
        nonlocal num
        num+=10
        print(num)
    b()
a()

# [-----------------------------------------------------]

# Q-10

def subject():
    return["Python","JS","Html"]

sub=subject()
print(sub)

sub.append("CSS")
sub[0] = "Maths"
print(sub)

# [-----------------------------------------------------]

# Q-11

count = 0
def increment():
    global count
    count += 1
    return count
print(increment())
print(increment())
print(increment())

# [-----------------------------------------------------]

# Q-12

x=1
def outer():
    x=2
    def inner():
        x=3
        print(x)
    inner()
    print(x)
outer()
print(x)

Out_put = """3
            2
            1"""

# [-----------------------------------------------------]

# Q-13

ans = "for loop does not create a separate scope but list has it's own scope"

# [-----------------------------------------------------]

# Q-14
def outer():
    message = "Hello Python"

    def inner():
        print(message)

    return inner


result = outer()
result()

# [-----------------------------------------------------]

# Q-15

ans = "it's already a keyword( Built - in Function) "

# [-----------------------------------------------------]