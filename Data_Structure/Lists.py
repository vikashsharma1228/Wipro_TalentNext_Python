# Write a program to create a list of 5 integers and display the list items. Access individual elements through index.

lis1 = [1, 2, 3, 4, 5]
print(lis1[0])
print(lis1[1])
print(lis1[2])
print(lis1[3])
print(lis1[4])



# Write a program to append a new item to the end of the list.

list2 = [1, 2, 3, 4, 5]
list2.append(6)
print(list2)


# Write a program to reverse the order of the items in the list.

list3 = [1, 2, 3, 4, 5]
list3.reverse()
print(list3)


# Write a program to print the number of occurrences of a specified element in a list.

list4 = [1, 2, 3, 4, 5,5,5]
print(list4.count(5))



# Write a program to append the items of list1 to list2 in the front.

list5 = [1, 2, 3, 4, 5]
list6 = [6, 7, 8, 9, 10]
list5.extend(list6)
print(list5)



# Write a program to insert a new item before the second element in an existing list.

list1 = [1, 2, 3, 4, 5]
list1.insert(1, 6)
print(list1)



# Write a program to remove the item from a specified index in a list.

list1 = [1, 2, 3, 4, 5]
list1.pop(2)
print(list1)



# Write a program to remove the first occurrence of a specified element from a list.

list1 = [1, 2, 3, 4, 5]
list1.remove(3)
print(list1)