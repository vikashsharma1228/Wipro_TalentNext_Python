# taking 2 number from user and dividing and thrwoing error messages 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
try:
    print(a/b)
except Exception as e:
    print(e)


# input from user and check if it is a prime or not or return exception when inputing other than int

a = int(input("Enter the number: "))

try:
    for i in range(2, a):
        if(a % i == 0):
            raise Exception("Not Prime")
    print("Prime")
except Exception as e:
    print(e)


# input from user that accepts a file name to be opened if exist print contents else error

file_name = input("Enter the file name: ")
try:
    f = open(file_name, "r")
    print(f.read())
    f.close()
except Exception as e:
    print(e)

# list with size and ask user to enter index and check it is positive or negative. if invalid index return error

list1 = [1, 2, 3, 4, 5,-1,-5,-10,9, 11]
index = int(input("Enter the index: "))
try:
    # print(list1[index])
    if(list1[index] >= 0):
        print("Positive")
    else:
        print("Negative")
except Exception as e:
    print(e)