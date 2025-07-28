# List and List Comprehension using python programming
# Write a python program that takes a list and returns a new list containing every second element from original list
def one():
    l = []
    length = int(input("Enter the length of the list: "))
    for i in range(length):
        l.append(int(input(f"Enter element {i+1}: ")))
    nl = []
    for i in range(len(l)):
        if i % 2 != 0:
            nl.append(l[i])
    print(nl)
# Write a python program that finds and returns the largest element in the list
def two():
    l = []
    length = int(input("Enter the length of the list: "))
    for i in range(length):
        l.append(int(input(f"Enter element {i+1}: ")))
    print(max(l))
# Write a python program that takes a list as an input from the user with 8 different countries as data, manipulate the
# list with 7 different methods and print the output
def three():
    l = []
    length = 8
    for i in range(length):
        l.append(input(f"Enter Country {i+1}: "))
    print("Original List:", l)
    print("Accessing 3rd element:", l[2])
    print("Slicing first 5 elements:", l[:5])
    l.append("New Country")
    print("After Appending:", l)
    l.insert(2, "Inserted Country")
    print("After Inserting at index 2:", l)
    l.remove("New Country")
    print("After Removing 'New Country':", l)
    l.sort()
    print("After Sorting:", l)
    l.reverse()
    print("After Reversing:", l)
    search = input("Enter a country to search: ")
    if search in l:
        print(f"{search} found at index {l.index(search)}")
    else:
        print(f"{search} not found in the list")
# Write a python program using list comprehension to create a new list containing only even numbers from a user input list
def four():
    l = []
    length = int(input("Enter the length of the list: "))
    for i in range(length):
        l.append(int(input(f"Enter element {i+1}: ")))
    nl = [i for i in l if i % 2 == 0]
    print("New List:", nl)
#  Write a python program that takes two different lists and returns a new list containing only the elements that are
#  common between the two lists.
def five():
    l1 = ['Orange', 'Apple', 'Banana', 'Grapes', 'Blueberry']
    l2 = ['Orange', 'Apple', 'Strawberry', 'Guava', 'Cherry']
    common = [item for item in l1 if item in l2]
    print("Common elements:", common)
# Write a python program that finds all pairs of integers in a list whose sum is equal to a given number.
# Given List = [2,4,3,5,7,8,9], Given Number = 7
# Output should be [(2,5),(4,3)]
def six():
    l = [2,4,3,5,7,8,9]
    num = 7
    pl = []
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] + l[j] == num and i != j:
                if (l[i], l[j]) not in pl and (l[j], l[i]) not in pl:
                    pl.append((l[i], l[j]))
    print("Pairs with sum", num, ":", pl)
# Write a python program that takes a user input integer list and manipulate the list with 6 different list
# functions and print the output
def seven():
    l = []
    length = int(input("Enter the length of the integer list: "))
    for i in range(length):
        l.append(int(input(f"Enter element {i+1}: ")))
    print("Original List:", l)
    print("Length of List:", len(l))
    print("Maximum Element:", max(l))
    print("Minimum Element:", min(l))
    print("Sum of Elements:", sum(l))
    print("Average of Elements:", sum(l) / len(l))
    print("Sorted List:", sorted(l))