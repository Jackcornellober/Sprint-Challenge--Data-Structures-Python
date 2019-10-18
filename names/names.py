# import time

# from binary_search_tree import BinarySearchTree

# start_time = time.time()

# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

# binary = BinarySearchTree(names_2[0])

# for index,i in enumerate(names_2):
#     if index == 0:
#         pass
#     else:
#         binary.insert(i)


# duplicates = []
# for name_1 in names_1:
#     if binary.contains(name_1):
#         duplicates.append(name_1)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

import time

from timsort import TimSort, binary_sort

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

sorted = TimSort(names_2)
duplicates = []

for i in names_1:
    if binary_sort(sorted,len(sorted),i) == True:
        duplicates.append(i)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")