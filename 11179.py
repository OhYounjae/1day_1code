n = int(input())
first_num = bin(n)
for i in range(len(first_num)//2):
    num = first_num[i]
    first_num[i] = first_num[-i]
    first_num[-i] = num
