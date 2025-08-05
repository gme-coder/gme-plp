# creating a list called my_list
my_list =[]

#appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)      
my_list.append(40)

#inserting the value 15 at the second position in the list
my_list.insert(1, 15)

# extending my_list with another list[50, 60 70]
my_list.extend([50, 60, 70])

# removing the last element  fro my_list
my_list.pop()

# sort my_list in ascending order
my_list.sort()  

#find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(f"Index of 30 in my_list: {index_of_30}")

