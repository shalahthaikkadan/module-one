l1 = [1,2,3]
l2 = []
def new_mult():
    for i in l1:
        result = i * 2
        l2.append(result)
new_mult()
print(l2)
