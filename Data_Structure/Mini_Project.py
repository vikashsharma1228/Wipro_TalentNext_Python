# 1.  Create a dictionary that contains a list of people and one interesting fact about each of them.
# Display each person and his or her interesting fact to the screen. Next, change a fact about one of the people. Also add an additional person and corresponding fact. Display the new list of people and facts. Run the program multiple times and notice if the order changes

people = {
    "Vikash": "I like to play cricket",
    "Ankit": "I like to play badminton",
    "Ankit": "Afraid of cats",
    "David": "Plays the piano",
    "Jason": "Can fly an airplane"
}

for person, fact in people.items():
    print(person,": ", fact)


# 2. runner up score form a list and find score of runneer up


scores = [1, 2, 3, 4, 5, 6, 6, 8, 9, 10]
scores.sort()
print(scores[-2])

# 3. student and her marks of 3 subject return user after search and return its average numbers

marks = {
    "Vikash": [20, 30, 40],
    "Ankit": [50, 60, 70],
    "David": [80, 90, 100]
}


def get_average_marks(student_name):
    if student_name in marks:
        return sum(marks[student_name]) / len(marks[student_name])
    else:
        return "Student not found"
    
name = input("Enter student name: ")
average_marks = get_average_marks(name)
print("Average marks for", name, "is", average_marks)


# 4. how many time words appear in string

def word_count(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

word = input("Enter the sentence: ")
print(word_count(word))