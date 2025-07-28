# Module for Plaindrome, no. of vowels and frequency of letters

def plaindrome(word):
    if word == word[::-1]:
        return "Yes"
    else:
        return "No"

def vowel_count(word):
    count = 0
    for i in word:
        if i in "aeiouAEIOU":
            count += 1
    return count

def frequency(word):
    freq = {}
    for i in word:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

