# Q-1

# def show(n):
#     if n == 0:
#         print("Stop")
#         return

#     print(n)
#     show(n - 1)
#     print(n)

# show(2)

# ----------> 2
#             1
#             stop
#             1
#             2


#Q-2

# def total(n):
#     if n == 0:              #Base-case
#         return 0            #Base-case

#     return n + total(n - 1)


# Q-3

#Wrong-code
# def count(n):
#     if n == 0:
#         return

#     count(n + 1)
# count(2)

# mistake in this code is when we write recursive case we have to insure that recursive case hepl base case to stop.

#Right-code
# def count(n):
#     if n == 0:
#         return

#     count(n - 1)

# Q-4

# def answer(n):
#     if n == 0:
#         return 0

#     n + answer(n - 1)

# print(answer(3))
# we can see in this code that return is not writen so when we see this code in backend than it will give none and on 55 line it writen (number + none ) both have different datatype so it will give typeerror.


# Q-5

# def countdown(n):
#     if n==0:
#         print("Done")
#         return
#     print(n)
#     countdown(n-1)
# countdown(3)

# Q-6

# def count_up(n):
#     if n==0:
#         return 0
#     count_up(n-1)
#     print(n)
# count_up(4)

# Q-7

# add=0
# def counter_fun(n):
#     global add
#     add+=n
#     if(n==5):
#         return add
#     return counter_fun(n+1)
# print(counter_fun(1))

# Q-8
# def factorial(n):
#     if (n==0):
#         return 1
#     return n*factorial(n-1)
# print(factorial(4))
# print(factorial(0))

# Q-9

# def digit_sum(n):
#     if n<10:
#         return n
#     return n%10 + digit_sum(n//10)
# print(digit_sum(583))  #5+8+3=16
# print(digit_sum(7))    # 7 less than 10 hai to direct 7 print
# print(digit_sum(0))    # similiarlly

# Q-10

# def power(n,m):
#     if(m==0):
#         return 1
#     return n**m
# print(power(2,5))
# print(power(9,0))
# print(power(3,1))

# Q-11

# def count_digit(n):
#     if (n<10):
#         return 1
#     return 1+count_digit(n//10)
# print(count_digit(5382))
# print(count_digit(6))
# print(count_digit(0))

# Q-13

# def fibonacci(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(6))

# Q-14

# def max_digit(n):
#     if n==0:
#         return 0
#     return n%10
# print(max_digit(4729))
# print(max_digit(0))
# print(max_digit(555))

# Q-15

# def mystery(n):
#     if n<=1:
#         return n
#     return mystery(n-1)+mystery(n-2)
# print(mystery(4))
#print(mystery(0))
# print(mystery(1))
# print(mystery(2))
 #sol: mystery(4)
#  mystery(3)+mystery(2)
# [mystery(2)+mystery(1)]+1
# [1+1]+1
# 2+1=3 
# final output:4
#              Section D — Edge Cases and Debugging (10 marks)

# Q-16

# def factorial(n):
#     if n==0:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

# Q-17

# def stop_at_zero(n):
#     if n==0:
#         return
#     print(n)
#     stop_at_zero(n-1)
# stop_at_zero(5)

# Q-18
# Agar recursion ka base case fullfill na ho to recursive error aayega recursice case ka matlb base case ki taraf.
