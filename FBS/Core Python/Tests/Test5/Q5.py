#Python Program to Find the Union of two Lists without
#using set concept.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

union = []

for x in list1:
    if x not in union:
        union.append(x)

for x in list2:
    if x not in union:
        union.append(x)

print("List 1:", list1)
print("List 2:", list2)
print("Union:", union)