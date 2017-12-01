#설탕 배달 문제
n = int(input())

"""
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
"""

a = n % 5
b = n // 5
c = n - (5 * b)

if a == 0 :
    print(b)
elif a != 0 :
    if c % 3 == 0:
        print(b + (c // 3))

    elif c % 3 != 0 :
        print(-1)