# 1. write a function to return the sum of all number in a list


def sumList(list1):
    sum = 0
    for i in list1:
        sum += i
    return sum

list1 = [1, 2, 3, 4, 5]
print(sumList(list1))


# 2. Write a function to return the reverse of a string

def reverse(string):
    return string[::-1]

string = "Vikash"
print(reverse(string))


# 3. Write a function to calculate and return the fac of a number

def fact(a):
    fact = 1
    for i in range(1, a + 1):
        fact *= i
    return fact

a = int(input("Enter the number: "))
print(fact(a))


# 4. Function that accepts a string and prints the number of upper case and lower case letters

def count(string):
    upper = 0
    lower = 0
    for i in string:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
    return upper, lower

string = "viKash"
print(count(string))


# 5. print even numbers from a given list 

def evencount(list):
    count = 0
    for i in list:
        if i%2 == 0:
            count += 1
    return count

list = [1, 2, 3, 4, 5]
print(evencount(list))


# 6. prime or not 

def prime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

a = 5
print(prime(a))