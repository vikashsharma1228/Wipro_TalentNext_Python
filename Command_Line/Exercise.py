# 1. accept 2 argument and return sum

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(a + b)

# 2. accept a welcome message and display file name along with the welcome messgae

message = input("Enter the message: ")
file_name = input("Enter the file name: ")
print(message, file_name)

# 3. to accept 10 argument and print sum of prime numbers among them

num = []
sum = 0

for i in range(10):
    num.append(int(input("Enter the numbers: ")))

for i in num:
    for j in range(2, i):
        if(i % j == 0):
            break
    else:
       sum += i

print(sum)

