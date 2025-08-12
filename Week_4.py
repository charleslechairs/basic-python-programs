# Week 4 - Control Structures

# WAP that takes a number from the user and checks if the number if its divisible by both 3 and 5
def one():
    num = int(input("Enter a number: "))
    if (num%3==0 and num%5==0):
        print("Number divisible by both 3 and 5")
    else:
        print("Number not divisible by both 3 and 5")

# WAP to print all the even number numbers between 1 and 20
def two():
    for i in range(2,20):
        if (i%2 == 0):
            print(i)

# WAP that prints numbers from 1 to 10 but stops when it reaches 6
def three():
    for i in range(1,11):
        if i < 6:
            print(i)
        else:
            break

# WAP prints numbers from 1 to 10 skipping the multiples of 3
def four():
    for i in range(1,11):
        if (i%3 != 0):
            print(i)

# WAP to simulate an ATM machine with the follwoing features - Pin verification (3 attempts max), 
# Menu options (Balance, Withdraw, Deposit, Mini Statements of last 5 transactions, Exit), 
# Apply the conditions for valid withdrawal (Amount >= 0, >= Balance, Multiples of 100), 
# for valid deposit (Amount >0), Use if,else,for,while,break,continue at least once in the program
def five():
    bal = 0
    pin = 2007
    stat = []
    attempts = 1
    verf = False
    while attempts < 4:
        inp = int(input("Enter your 4-digit PIN: "))
        if inp == pin:
            verf = True
            break
        else:
            print(f"Wrong pin try again {3-attempts} attempts left")
            attempts += 1
            if attempts == 4:
                print("Your account has been blocked")
    print("Welcome to ATM\n1.Check balance\n2.Withdraw\n3.Deposit\n4.Mini Statement of last 5 transactions\n5.Exit")
    while verf:
        ch = int(input("Enter your choice: "))
        if ch == 1:
            print(f"Your balance is {bal}")
        elif ch == 2:
            if bal <= 0:
                print("You dont have any balance in account to withdraw")
                continue
            else:
                amt = int(input("Enter amount to withdraw: "))
                if amt > 0 and amt%100 == 0:
                    bal -= amt
                    stat.append(-amt)
                    print(f"Successfully withdrew {amt}, Current balance = {bal}")
                else:
                    print("Unable to withdraw make sure amount is in multiples of 100")
        elif ch == 3:
            amt = int(input("Enter amount to deposit: "))
            if amt <= 0:
                print("Enter a valid amount")
                continue
            else:
                bal += amt
                stat.append(amt)
                print(f"Succesfully deposited {amt}, Current balance = {bal}")
        elif ch == 4:
            if len(stat) == 0:
                print("No statements in account")
            elif len(stat) <= 5:
                print(f"Last five statements : {stat[::-1]}")
            else:
                print(f"Last five statements: {stat[:-6:-1]}")
        elif ch == 5:
            print("Thank you for using the ATM")
            break
        else:
            print("Invalid choice try again")
