#1

# n=int(input("Enter a number: "))
# n=abs(n)
# count=0
# if n==0:
#     count=1
# else:
#     while n>0:
#         count+=1
#         n=n//10
# print(count)

#2

# n=int(input("Enter a numer :"))
# n=abs(n)
# sum=0
# while n>0:
#     digit=n%10
#     sum+=digit
#     n=n//10
# print("sum of total digits: ", sum)

#3

# n=int(input("Enter a numer :"))
# n=abs(n)
# multiple=1
# while n>0:
#     digit=n%10
#     multiple*=digit
#     n=n//10
# print("multiple of total digits: ", multiple)

#4

# n=int(input("Enter a number :"))
# rev=0
# while n>0:
#     digit=n%10
#     rev=(rev * 10) + digit
#     n=n//10
# print(rev)

#5

# str=input("Enter a number :").strip().lower()
# j=len(str)-1
# i=0
# flag=True
# while i<j:
#     if str[i]!=str[j]:
#         flag=False
#     i+=1
#     j-=1
# if flag:
#     print("String is palindrome ")
# else:
#     print("String is not palindrome ")

#6

# n=int(input("Enter a number : "))
# if n<=1:
#     print("false")
# elif n==2:
#     print("true")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("false")
#             break
#     else:
#         print("true")

#7

# n=int(input("Enter a number : "))
# for i in range(2,n+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

#8

# n=int(input("Enter a number : "))
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c

#9

# a=int(input("Enter first number : "))
# b=int(input("Enter second number : "))
# for i in range(1,min(a,b)+1):
#     if a%i==0 and b%i==0:
#         gcd=i
# print("GCD = ",gcd)

#10

# a=int(input("Enter first number : "))
# b=int(input("Enter second number : "))

# for i in range( max(a,b) , (a*b) +1):
#     if i % a == 0 and i % b == 0:
#         print("LCM = ",i)
#         break