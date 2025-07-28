# 1. Write a program to check if a given number is Positive, Negative or Zero.

num = int(input("Enter the number: "))

if(num > 0):
    print("Number is positive")
elif(num < 0):
    print("Number is negative")
else:
    print("Number is zero")

# 2. Write a program to check if a given number is odd or even.

num = int(input("Enter the number to check for even & odd: "))
if(num % 2 == 0):
    print("Number is even")
else:
    print("Number is odd")


# 3.  Given two non-negative values, print true if they have the same last digit, such as with 27 and 57

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if(num1 % 10 == num2 % 10):
    print("True")
else:
    print("False")

# 4. Write a program to print numbers from 1 to 10 in a single row with one tab space. 

for i in range( 11):
    print(i+1, end="\t")

# 5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.

for i in range(23, 57):
    if(i % 2 == 0):
        print(i)


# 6.  Write a program to check if a given number is prime or not.

num = int(input("Enter the number to check for prime or not: "))

for i in range(2, num):
    if(num % i == 0):
        print("Number is not prime")
        break
else:
    print("Number is prime")

# 7. Write a program to print prime numbers between 10 and 99.

for i in range(10, 100):
    for j in range(2, i):
        if(i % j == 0):
            break
    else:
        print(i)

# 8.Write a program to print the sum of all the digits of a given number.

num = int(input("Enter the number: "))

sum = 0
while(num > 0):
    rem = num % 10
    sum = sum + rem
    num = num / 10

print(int(sum))

# 9. Write a program to reverse a given number and print.

num = int(input("Enter the number: "))
rev = 0

while(num > 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

print(rev)

# 10. Write a program to find if the given number is palindrom or not

num = int(input("Enter the number: "))
rev = 0

while(num > 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if(rev == num):
    print("Number is palindrom")
else:
    print("Number is not palindrom")
