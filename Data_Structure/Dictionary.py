#1. Add key and value to dictionary at output

dict = {
    0: 10,
    1 : 20,
    2 : 30
}

print(dict)
dict[3] = 40
print(dict)

# --------------------------------------------

# 2. concatenate dictionaries

dict1 = {
    1: 10,
    2: 20
}
dict2 = {
    3: 30,
    4: 40
}
dict3 = {**dict1, **dict2}
print(dict3)

# --------------------------------------------

# 3. check is a key is exists in dict1
dict1 = {
    0: 10,
    1 : 20,
    2 : 30
}

a = int(input("Enter the key: "))

if(a in dict1):
    print("True")
else:
    print("False")

# ---------------------------------------------

#4.  iterate over dict using for loop and print key and value

dict1 = {
    0: 10,
    1 : 20,
    2 : 30,
    4: 40,
}
print('Keys: ', dict1.keys())
print('Values: ', dict1.values())
for i in dict1:
    print(i, dict1[i])

# --------------------------------------------------

# 5. sum of values in dict

dict1 = {
    0: 10,
    1 : 20,
    2 : 30,
    4: 40,
}
sum = 0
for i in dict1:
    sum += dict1[i]
print(sum)