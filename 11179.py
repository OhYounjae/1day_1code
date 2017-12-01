n = int(input())
first_num = bin(n)
#print(first_num)
sec_num = first_num[2::]
#print(sec_num)

third_num = sec_num[::-1]
#print(third_num)

last_num = int(third_num, 2)
#print(last_num)


"""
# str is immutable type

for i in range(len(first_num)//2):
    num = first_num[i]
    first_num[i] = first_num[-i]
    first_num[-i] = num
"""