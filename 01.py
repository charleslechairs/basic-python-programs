# Title - Basic numerical operations using pythpn
import math
def one():
    print(5)
    print("x=5")
    x=5
    print("x+1")
    print(x+1)

def cost():
    carrot_cost = 10
    apple_cost = 20
    tot_cost = (5*carrot_cost) + (4*apple_cost)
    print("Cost of 5 carrot and 4 apples:",tot_cost)


def dist():
    first = input("Enter coords 1 sep by space:")
    second = input("Enter coords 2 sep by space:")
    f1 = first.split(" ")
    f2 = second.split(" ")
    x1,y1,z1 = int(f1[0]), int(f1[1]), int(f1[2])
    x2,y2,z2 = int(f2[0]), int(f2[1]), int(f2[2])
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print("Distance between two points:",round(distance,2))


def sqr():
    num = int(input("Enter a number:"))
    print("Square of", num, "is", num**2)

def rem():
    n1 = int(input("Enter first number:"))
    n2 = int(input("Enter second number:"))
    quot = n1//n2
    reminder = n1%n2
    print("quotetint:",quot, "Remainder:",reminder)


def avg():
    n1 = int(input("Enter first number:"))
    n2 = int(input("Enter second number:"))
    n3 = int(input("Enter third number:"))
    total = n1+n2+n3
    average = total/3
    print("Total:", total, "Average:", average)

def under():
    str = input("Enter a string:")
    news = str.replace(" ", "_")
    print("String with underscores:", news)

def palin():
    str = input("Enter a string:")
    if str == str[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

def concat():
    str1 = input("Enter first string:")
    str2 = input("Enter second string:")
    news = str1 + str2
    print("Concatenated string:", news)
    print("Length of final string:", len(news))

def hwd():
    height = 12
    width = 17
    delimiter = 5
    print("Height/3:", height/3, "\t",type(height/2))
    print("Width/2:", width/2, "\t", type(width/2))
    print("Delimiter*5:", delimiter*5, "\t", type(delimiter*2))


def mod():
    roll = 5004
    print("Roll:", roll)

def exp():
    x = 28
    print("x:", x)
    print("x+1=",eval("x+1"))
    print("x-2=",eval("x-2"))
    print("x*2=",eval("x*2"))
    print("x/2=",eval("x/2"))

def revstr():
    string = input("Enter a string: ")
    ls = string.split(' ')
    ls.reverse()
    print(' '.join(ls))


def smallencrp():
    message = input("Enter a message to encrypt: ")
    encrypted_message = ''.join(chr(ord(char) + 3) for char in message)
    print("Encrypted message:", encrypted_message)

    decrypted_message = ''.join(chr(ord(char) - 3) for char in encrypted_message)
    print("Decrypted message:", decrypted_message)

def flames():
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")
    for i in name1:
        for j in name2:
            if i == j:
                name1 = name1.replace(i, "", 1)
                name2 = name2.replace(j, "", 1)
                break
    count = len(name1) + len(name2)
    print(name1, name2, "Count:", count)
    flames_list = ["Friends", "Love", "Albon", "Mbappe", "Enemy", "Siblings"]
    ind = 0
    while len(flames_list) > 1:
        ind = (ind + count - 1) % len(flames_list)
        flames_list.pop(ind)
    print("Result:", flames_list[0])

def anagram():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    if sorted(str1) == sorted(str2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

def odd_even():
    string = input("Enter a string: ")
    odd = []
    even = []
    for i in range(len(string)):
        if i % 2 == 0:
            odd.append(string[i])
        else:
            even.append(string[i])
    odd = ''.join(odd)
    even = ''.join(even)
    print("Characters at odd positions:", odd)
    print("Characters at even positions:", even)

def alphabetical_order():
    string = input("Enter a string: ")
    words = list(string)
    words.sort()
    print("Words in alphabetical order:", ''.join(words))
