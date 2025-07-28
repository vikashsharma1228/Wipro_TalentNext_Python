#1. remove given item from set

set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)


#2. intersection of sets

set2 = {1, 2, 3, 4, 5}
set3 =  {4, 5, 6, 7, 8}

set4 = set2.intersection(set3)
print(set4)

# 3. union of sets

set5 = {1, 2, 3, 4, 5}
set6 =  {4, 5, 6, 7, 8}

set7 = set5.union(set6)
print(set7)

# max and min in set

set8 = {1, 2, 3, 4, 5}
print(max(set8))
print(min(set8))