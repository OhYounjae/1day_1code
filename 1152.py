n = str(input())
strings = n.split(" ")
count = len(strings)
for i in range(len(strings)):
    if strings[i] == str(''):
        count -= 1
print(count)

