# Write a program to print the 4th element from first and 4th element from last in a tuple.

tup1 = (1, 2, 3, 4, 5)

print(tup1[3])
print(tup1[-4])


# Write a program to check whether an element exists in a tuple or not.

tup2 = (1, 2, 3, 4, 5)
print(3 in tup2)


# Write a program to convert a list into a tuple.

tup3 = [1, 2, 3, 4, 5]

print(tuple(tup3))



# Write a program to find the index of an item in a tuple.

tup4 = (1, 2, 3, 4, 5)
print(tup4.index(3))


# Write a program to replace last value of tuples in a list to 100. 

tup5 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

for i in range(len(tup5)):
    tup5[i] = list(tup5[i])
    tup5[i][-1] = 100
    tup5[i] = tuple(tup5[i])
print(tup5)