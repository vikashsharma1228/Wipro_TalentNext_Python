# Through command line arguments three strings separated by space are given to you. Each string is a series of numbers separated by hyphen(-). You like all the numbers in string 1 and dislike all the numbers in string 2.
# Third string contains the numbers given to you. Your initial happiness is 0. When you encounter a number which is present in string 1, add 1 to your happiness, if it is present in string 2, add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
string3 = input("Enter the third string: ")

happiness = 0

for i in string3.split("-"):
    if i in string1.split("-"):
        happiness += 1
    elif i in string2.split("-"):
        happiness -= 1

print(happiness)