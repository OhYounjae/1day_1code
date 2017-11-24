n = str(input())
obstacle = 0

for i in range(len(n)):
    print(n[i], end ='')
    obstacle += 1
    if obstacle == 10:
        print()
        obstacle = 0



"""
string = list(input())
b = len(string)
c = b // 10
i = 0
j = i + 10
print(''.join(string[i:j]))

for k in range(c):
    i += 10
    j += 10
    print(''.join(string[i:j]))"""