#설탕 배달 문제
n = int(input())

a = n // 5
b = (n - (a * 5)) // 3
c = (n - (a * 5)) % 3

if n % 5 != 0:
    if c != 0:
        print("-1")
    elif c == 0:
        print(a + b)
elif n % 5 == 0:
    print(a)