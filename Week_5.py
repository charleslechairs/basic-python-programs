# Write an array structure that contains the marks of 20 students, then do the following operations with numpy
import numpy as np
marks = np.array([45,78,62,89,90,55,38,100,67,73,82,49,95,60,71,85,77,53,92,68])
# Display the total number of students
print("Total number of students:", marks.size)
# Print all the marks with the indexes
for i in range(len(marks)):
    print("Student", i+1, "marks:", marks[i])
# Access and print the 5th student marks
print("Student 5 marks:", marks[4])
# Slice and print the marks of students from index 5 to 10
print("Marks from student 6 to 11:", marks[5:11])
# Insert a new mark 88 at 10th position
marks = np.insert(marks, 9, 88)
print("Marks after inserting 88 at 10th position:", marks)
# Append a new mark 40 at the end
marks = np.append(marks, 40)
print("Marks after appending 40 at the end:", marks)
# Delete the first occurence of mark 55 without deleting other 55's
marks = np.delete(marks, np.where(marks == 55)[0][0])
print("Marks after deleting first occurrence of 55:", marks)
# Remove the mark at index 3
marks = np.delete(marks, 3)
print("Marks after removing mark at index 3:", marks)
# Check if 100 exsists in the array
print("100 exists in the array:", 100 in marks)
# Count how many students scored exactly 90
print("Number of students scored 90:", np.sum(marks == 90))
# Find the index of first student who scored 71
print("Index of first student who scored 71:", np.argmax(marks == 71))
# Sort the marks in ascending and descending order
marks_ascending = np.sort(marks)
marks_descending = np.sort(marks)[::-1]
print("Marks in ascending order:", marks_ascending)
print("Marks in descending order:", marks_descending)

# Reverse the given array
marks_reversed = marks[::-1]
print("Reversed array:", marks_reversed)

# Find the maximum and minimum marks in given array
max_marks = np.max(marks)
min_marks = np.min(marks)
print("Maximum marks:", max_marks)
print("Minimum marks:", min_marks)

# Calculate sum and average of given marks
sum_marks = np.sum(marks)
average_marks = np.mean(marks)
print("Sum of marks:", sum_marks)
print("Average marks:", average_marks)

# Find the second highest and second lowest marks
unique_marks = np.unique(marks)
unique_marks_desc = np.sort(unique_marks)[::-1]
second_highest = unique_marks_desc[1] if len(unique_marks_desc) > 1 else "No second highest"
second_lowest = np.sort(unique_marks)[1] if len(unique_marks) > 1 else "No second lowest"
print("Second highest marks:", second_highest)
print("Second lowest marks:", second_lowest)

# Find the bottom 5 scores
bottom_5 = np.sort(marks)[:5]
print("Bottom 5 scores:", bottom_5)

# Count how many students scored more than 70
students_above_70 = np.sum(marks > 70)
print("Number of students scored more than 70:", students_above_70)

# Reshape the array into 4 rows and 5 columns
# Check if current array length allows reshaping to 4x5
if marks.size >= 20:
    # Take first 20 elements for reshaping
    marks_subset = marks[:20]
    reshaped_marks = marks_subset.reshape(4, 5)
    print("Marks reshaped into 4 rows and 5 columns:")
    print(reshaped_marks)
else:
    print("Array too small to reshape into 4x5")

# Split the array into 2 halves and print them
half1, half2 = np.array_split(marks, 2)
print("First half:", half1)
print("Second half:", half2)

"""
=== DETAILED EXPLANATION OF NUMPY FUNCTIONS USED ===

1. np.array([list]):
   - Creates a numpy array from a Python list
   - Example: np.array([1,2,3]) creates a 1D numpy array
   - More efficient than Python lists for numerical operations

2. array.size:
   - Returns the total number of elements in the array
   - For 1D array: same as length
   - For 2D array: rows × columns

3. np.insert(array, index, value):
   - Inserts a value at specified index position
   - Original array remains unchanged, returns new array
   - Example: np.insert([1,2,3], 1, 99) → [1,99,2,3]

4. np.append(array, value):
   - Adds value(s) to the end of array
   - Returns new array, original unchanged
   - Example: np.append([1,2,3], 4) → [1,2,3,4]

5. np.delete(array, index):
   - Removes element(s) at specified index/indices
   - Returns new array without deleted elements
   - Example: np.delete([1,2,3], 1) → [1,3]

6. np.where(condition):
   - Returns indices where condition is True
   - Example: np.where([1,2,3,2] == 2) → (array([1,3]),)
   - [0][0] gets the first occurrence index

7. np.sum(array) or np.sum(condition):
   - For numbers: calculates sum of all elements
   - For booleans: counts True values (True=1, False=0)
   - Example: np.sum([True,False,True]) → 2

8. np.argmax(array):
   - Returns index of first occurrence of maximum value
   - For boolean arrays: finds first True value
   - Example: np.argmax([1,3,2]) → 1 (index of max value 3)

9. np.sort(array):
   - Returns sorted copy of array in ascending order
   - Original array unchanged
   - [::-1] reverses to get descending order

10. Array slicing [::-1]:
    - Reverses array order
    - Start:Stop:Step notation
    - [::-1] means start to end with step -1 (backward)

11. np.max(array) and np.min(array):
    - Returns maximum/minimum value in array
    - More efficient than Python's max()/min() for large arrays

12. np.mean(array):
    - Calculates arithmetic mean (average) of array elements
    - Sum of all elements divided by number of elements

13. np.unique(array):
    - Returns sorted unique elements from array
    - Removes duplicates automatically
    - Example: np.unique([1,2,2,3]) → [1,2,3]

14. Boolean indexing (array > value):
    - Creates boolean array where condition is True/False
    - Example: [1,2,3] > 2 → [False,False,True]
    - Can be used with np.sum() to count matching elements

15. array.reshape(rows, cols):
    - Changes array shape without changing data
    - Total elements must remain same
    - Example: [1,2,3,4].reshape(2,2) → [[1,2],[3,4]]

16. np.array_split(array, sections):
    - Splits array into specified number of sub-arrays
    - Handles uneven splits automatically
    - Returns list of arrays

=== HOW BOOLEAN OPERATIONS WORK ===

When you use conditions like (marks == 90):
1. Python compares each element individually
2. Creates boolean array: [False, True, False, True, ...]
3. True = 1, False = 0 in numerical operations
4. np.sum() counts True values by adding 1s and 0s
5. np.argmax() finds first True (maximum value in boolean context)

Example with marks = [45, 90, 62, 90]:
- marks == 90 → [False, True, False, True]
- np.sum(marks == 90) → 0+1+0+1 = 2 (count)
- np.argmax(marks == 90) → 1 (first True at index 1)

=== MEMORY EFFICIENCY ===
- Numpy arrays store data in contiguous memory
- Operations are vectorized (applied to all elements simultaneously)
- Much faster than Python loops for large datasets
- Functions like np.sum(), np.mean() use optimized C code internally
""" 