#Tuples and Dictionaries in Python

# Remove duplicate values from a tuple but keep the original order.
def one():
    tup = (1,3,2,1,5,3,7,5)
    l = list(tup)
    seen = []
    for item in l:
        if item not in seen:
            seen.append(item)
    print(tuple(seen))

# Find Common Elements in Multiple Tuples
def two():
    tup = ((1,2,3),(2,3,4,5),(0,2,3,9))
    a,b,c = list(tup[0]),list(tup[1]),list(tup[2])
    common = []
    for item in a:
        if item in b and item in c:
            common.append(item)
    print(tuple(common))

# Given data = (10, 20, 30, 40, 50), unpack only the first and last elements into variables
def three():
    tup = (10,20,30,40,50)
    a,b = tup[0],tup[-1]
    print(a,b)

# Count how many times each element appears in a tuple.
def four():
    tup = (1, 2, 2, 3, 3, 3, 4)
    result = []
    for item in tup:
        x = (item,tup.count(item))
        if x not in result:
            result.append(x)
    print(tuple(result))

# Replace index 2 value with 100 in tuple (10, 20, 30, 40, 50)
def five():
    tup = (10, 20, 30, 40, 50)
    nt = list(tup)
    nt[2] = 100
    tup = tuple(nt)
    print(tup)

# Replace every even number in (1, 2, 3, 4, 5, 6) with 0 → (1, 0, 3, 0, 5, 0)
def six():
    tup = (1, 2, 3, 4, 5, 6)
    nt = list(tup)
    for i in range(len(nt)):
        if nt[i] % 2 == 0:
            nt[i] = 0
    tup = tuple(nt)
    print(tup)

# Sort ('apple', 'banana', 'kiwi') by last character → ('banana', 'apple', 'kiwi').
def seven():
    tup = ('apple', 'banana', 'kiwi')
    nl = list(tup)
    for i in range(len(nl)):
        for j in range(i+1,len(nl)):
            if nl[i][-1] > nl[j][-1]:
                nl[i], nl[j] = nl[j], nl[i]
    tup = tuple(nl)
    print(tup)

# Convert [(1, 2), (3, 4), (5, 6)] → [(2, 1), (4, 3), (6, 5)].
def eight():
    l = [(1, 2), (3, 4), (5, 6)]
    nl = []
    for item in l:
        nl.append((item[1], item[0]))
    print(nl)

# Convert ([1, 2], [3, 4], [5, 6]) → [(1, 3, 5), (2, 4, 6)]
def nine():
    l = ([1, 2], [3, 4], [5, 6])
    nl = []
    for i in range(2):
        t = []
        for item in l:
            t.append(item[i])
        nl.append(tuple(t))
    print(nl)

# Given [1, 2, 3, 4, 5, 6] group into tuple of tuples of size 2 → ((1, 2), (3, 4), (5, 6))
def ten():
    l = [1, 2, 3, 4, 5, 6]
    nl = []
    for i in range(0, len(l)-1, 2):
        nl.append((l[i], l[i+1]))
    print(tuple(nl))

# You have tuple (10, 20, 30) and list [1, 2, 3]. Add them elementwise → (11, 22, 33).
def eleven():
    tup = (10, 20, 30)
    l = [1, 2, 3]
    nl = []
    for i in range(len(tup)):
        nl.append(tup[i] + l[i])
    print(tuple(nl))

# From [(2, 4), (1, 2), (6, 8)], filter only tuples where all numbers are even
def twelve():
    lst = [(2, 4), (1, 2), (6, 8)]
    nl = []
    for item in lst:
        for x in item:
            if x % 2 != 0:
                break
        else:
            nl.append(item)
    nl = tuple(nl)
    print(nl)
