# Write a program to read the entire content from a txt file and display it to the user.'

f1 = open("test.txt", "r")
print(f1.read())
f1.close()


# Write a program to read first n lines from a txt file. Get n as user input.

n = int(input("Enter the number of lines: "))
f2 = open("test.txt", "r")
for i in range(n):
    print(f2.readline())
f2.close()


# Write a program to accept input from user and append it to a txt file.

f3 = open("test.txt", "a")
f3.write(input("Enter the text: "))
f3.close()



# Write a program to read contents from a txt file line by line and store each line into a list.

f4 = open("test.txt", "r")
lines = f4.readlines()
print(lines)
f4.close()


# Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.

f5 = open("test.txt", "r")
words = f5.read().split()
longest_word = max(words, key=len)
print(longest_word)
f5.close()


# Write a program to count the frequency of a user entered word in a txt file.

f6 = open("test.txt", "r")
text = f6.read()
word = input("Enter the word: ")
count = text.lower().count(word.lower())
print(count)
f6.close()