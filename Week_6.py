# Week 6: Data Handling
# 1- Create a program that manages a simple student notes text file
# The program should first create a new file and write some student notes into it 
# Append a few extra notes
# Read the full file content
# Read line by line using both readline() and a loop
# Read all lines into a list
# Show the file pointer position and use seek() to move it
# Close the file using both close function and with (context manager)
# 2 - Create a secret diary program using text files
# The program should ask the user to enter a password
# If the password is correct, show the menu
# Menu options - Write a new diary entry, Read all diary entries, Count how many words are in the diary, Show the Longest word written so far
# If password is wrong, deny access
# Diary entries must be appended (so old entries are not lost)

import csv
def one():
    with open('student_notes.txt', 'w') as f:
        f.write("Student Notes\n")
        f.write("Math: A\n")
        f.write("Science: B\n")
    with open('student_notes.txt', 'a') as f:
        f.write("History: C\n")
    with open('student_notes.txt', 'r') as f:
        print(f.read())
    with open('student_notes.txt', 'r') as f:
        line = f.readline()
        while line:
            print(line)
            line = f.readline()
    with open('student_notes.txt', 'r') as f:
        lines = f.readlines()
        print(lines)
    with open('student_notes.txt', 'r') as f:
        print(f.tell())
        f.seek(10)
        print(f.tell())
    f = open('student_notes.txt', 'r')
    print("Opened file using open()")
    f.close()
    with open('student_notes.txt', 'r') as f:
        print("Opened file using with")

def two():
    password = 2007
    user_input = int(input("Enter the password: "))
    if user_input == password:
        print("Access granted.")
        while True:
            print("Menu:")
            print("1. Write a new diary entry")
            print("2. Read all diary entries")
            print("3. Count words in the diary")
            print("4. Show longest word")
            print("5. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                entry = input("Write your diary entry: ")
                with open('diary.txt', 'a') as f:
                    f.write(entry + "\n")
            elif choice == "2":
                with open('diary.txt', 'r') as f:
                    print(f.read())
            elif choice == "3":
                with open('diary.txt', 'r') as f:
                    content = f.read()
                    word_count = len(content.split())
                    print("Word count:", word_count)
            elif choice == "4":
                with open('diary.txt', 'r') as f:
                    content = f.read()
                    words = content.split()
                    longest_word = ""
                    for word in words:
                        if len(word) > len(longest_word):
                            longest_word = word
                    print("Longest word:", longest_word)
            elif choice == "5":
                print("Exited")
                break
            else:
                print("Invalid choice.")
    else:
        print("Access denied.")

def three():
    # Create a csv file students.csv with names and marks
    with open('students.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Marks'])  # Header
        writer.writerow(['Alice', 85])
        writer.writerow(['Bob', 92])
        writer.writerow(['Charlie', 78])
    
    # Append a new student record entered by the user
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    with open('students.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, marks])
    
    # Read and display all the records
    print("\nAll student records:")
    with open('students.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def four():
    # Create a csv file marks.csv with the following structure: name, maths, science, english
    with open('marks.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Name', 'Maths', 'Science', 'English'])
        w.writerow(['Alice', 85, 90, 88])
        w.writerow(['Bob', 92, 87, 85])
        w.writerow(['Charlie', 78, 82, 90])
    
    # Read the csv file
    with open('marks.csv', 'r') as f:
        r = csv.DictReader(f)
        s = list(r)
    
    # Calculate the total marks for each student
    print("\nTotal marks for each student:")
    st = []
    for x in s:
        t = int(x['Maths']) + int(x['Science']) + int(x['English'])
        st.append((x['Name'], t))
        print(f"{x['Name']}: {t}")
    
    # Find the topper
    top = max(st, key=lambda x: x[1])
    print(f"\nTopper: {top[0]} with {top[1]} marks")
    
    # Calculate the average marks per subject
    tm = sum(int(x['Maths']) for x in s)
    ts = sum(int(x['Science']) for x in s)
    te = sum(int(x['English']) for x in s)
    n = len(s)
    
    print(f"\nAverage marks per subject:")
    print(f"Maths: {tm / n:.2f}")
    print(f"Science: {ts / n:.2f}")
    print(f"English: {te / n:.2f}")
    
    # Let the user search a student by name and show their marks
    sn = input("\nEnter student name to search: ")
    found = False
    for x in s:
        if x['Name'].lower() == sn.lower():
            print(f"\nMarks for {x['Name']}:")
            print(f"Maths: {x['Maths']}")
            print(f"Science: {x['Science']}")
            print(f"English: {x['English']}")
            found = True
            break
    
    if not found:
        print("Student not found!")
    
    # Append a new student record entered by the user
    print("\nAdd a new student:")
    nn = input("Enter student name: ")
    nm = int(input("Enter Maths marks: "))
    ns = int(input("Enter Science marks: "))
    ne = int(input("Enter English marks: "))
    
    with open('marks.csv', 'a', newline='') as f:
        w = csv.writer(f)
        w.writerow([nn, nm, ns, ne])
    
    print("New student record added successfully!")


mrk = {"A":203,"B":293,"C":291}
dic = {k.lower():v+192 for k,v in mrk.items()}
print(dic)