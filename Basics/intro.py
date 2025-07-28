# print("hello")
# print(23)

# print("hello", 23)

# print(2, 4, 6, 8, sep=" % ", end=" & \n") #2 % 4 % 6 % 8 &

# a = "Suyash";
# b = 23;
# print(a,b)
# print(type(b))
# print(type(a))

# c = int(input("Enter the value of a: ")) # by default its string
# print(c)

# float(), str(), bool(); type casting 

# print(type(c))
# d = int(c);
# print(type(d))

# a = float(input("Enter the value of a: "))
# b = float(input("Enter the value of b: "))
# sum = a + b
# print("Sum of A & B is : ", sum)

# Strings ------------------------------------------------------------- 
# name = "Suyash Mishra"
# print(name.find('S'))
# print(len(name))
# print(name.split(" "))

# IF ELSE--------------------------------------------------------------
# num = int(input("Enter a number : "))
# if(num < 0):
#     print("Negative")
# elif(num > 0):
#     print("Positive")
# else:
#     print("Zero")


# LOOPS ---------------------------------------------------------------
# for i in range(5):
#     print(i)


# a = "Suyash"
# for i in a:
#     print(i)


# i = 1;
# while(i <= 5):
#     print(i)
#     i = i + 1


# LISTS ----------------------------------------------------------------
# marks = [20, 40, 30, 50]
# for i in marks:
#     print(i)


# marks.append(90)
# print(marks)

# marks.sort()
# print(marks)

# TUPLES ----------------------------------------------------------------
# marks = (20, 40, 30, 50)
# for i in marks:
#     print(i)

# print(marks.count(20))


# SETS ------------------------------------------------------------------

# marks = {20, 40, 30, 20}
# for i in marks:
#     print(i)

# DICTIONARY ------------------------------------------------------------------
# marks = {1:20, 2:40, 3:30}
# for i in marks:
#     print(i)


# print(marks.keys())
# print(marks.values())
# print(marks.items())


# FUNCTIONS --------------------------------------------------------------

def sum(a, b):
    print("Sum of A & B is : ", a + b)

sum(2, 3)