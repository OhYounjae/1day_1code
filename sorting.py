def findmin(lst):
    min_num = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min_num:
            min_num = lst[i]
    return min_num

a = [4, 1, 5, 3, 2]
b = []

for j in range(len(a)):
    result = findmin(a)
    b.append(result)
    print(b)
    a.remove(result)
    print(a)

print(a)
print(b)