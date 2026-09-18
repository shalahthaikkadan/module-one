l1 = [[1,2,3,4]]
l2 = []
for i in l1:
    for j in i:
        l2.append(j)
print(l2)
print([j*2 for i in l1 for j in i])