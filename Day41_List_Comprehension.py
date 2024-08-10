#     List Comprehension with String List:

# List Comprehension using Nested Loops

# List Comprehension with Multiple if Conditions

# List Comprehension with if-else Condition

#       Flatten List using List Comprehension:One of the applications of list comprehension is to flatten a list comprising of multiple lists into a single list.











names = ['Steve', 'Bill', 'Ram', 'Mohan', 'Abdul']
names2 = [s for s in names if 'a' in s]
print(names2)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums=[(x,y) for x in nums1 for y in nums2]
print(nums)



nums = [x for x in range(21) if x%2==0 if x%5==0] 
print(nums)



odd_even_list = ["Even" if i%2==0 else "Odd" for i in range(5)]
print(odd_even_list)
odd_even_list = [str(i) + '=Even' if i%2==0 else str(i) + "=Odd" for i in range(5)]
print(odd_even_list)




matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatList=[num for row in matrix for num in row]
print(flatList)


# Flatten List using Nested for Loop:
nestedlist = [ [1, 2, 3, 4], ["Ten", "Twenty", "Thirty"], [1.1,  1.0E1, 1+2j, 20.55, 3.142]]
flatlist=[]
for sublist in nestedlist:
    for element in sublist:
        flatlist.append(element)
print(flatlist)


nestedlist = [ [1, 2, 3, 4], ["Ten", "Twenty", "Thirty"], [1.1,  1.0E1, 1+2j, 20.55, 3.142]]
flatlist=[element for sublist in nestedlist for element in sublist]
print(flatlist)


