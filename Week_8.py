import statis
l = []
len_l = int(input("Enter the number of elements in the list: "))
for i in range(len_l):
    l.append(int(input(f"Enter element {i + 1}: ")))
print("Mean:", statis.mean_eshan(l))
if statis.mode_eshan(l) == 0:
    print("Mode: No mode found")
elif len(statis.mode_eshan(l)) == 1:
    print("Mode:", statis.mode_eshan(l)[0])
else:
    print("Mode:", statis.mode_eshan(l))
print("Unsorted List Median:", statis.median_eshan(l))
l.sort()
print("Sorted List Median:", statis.median_eshan(l))
print("Variance:", statis.stdvar_eshan(l))
print("Standard Deviation:", statis.stddev_eshan(l))

