# Write a program to count the number of upper and lower case letters in a String.

word = input("Enter the word: ")
count_upper = 0
count_lower = 0
for i in word:
    if i.isupper():
        count_upper += 1
    elif i.islower():
        count_lower += 1
print("Upper: ", count_upper)
print("Lower: ", count_lower)




# Write a program that will check whether a given String is Palindrome or not.
word2 = input("Enter the word: ")

if(word2 == word2[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")



# Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string. The string length will be >=2.

word3 = input("Enter the word: ")
print(word3[:2] * len(word3))

# Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi".

word4 = input("Enter the word: ")
if(word4[0] == 'x'):
    print(word4[1:])
elif(word4[-1] == 'x'):
    print(word4[:-1])
else:
    print(word4)


# Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string inclusive. For example if the inputs are "Wipro" and 3, then the output should be "propropro".

word5 = input("Enter the word: ")
n = int(input("Enter the number: "))
print(word5[-n:] * n)