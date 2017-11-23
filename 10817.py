a, b, c = map(int, input().split())

if a >= b and a >= c:
    if b >= c:
        print(b)
    elif c >= b:
        print(c)

elif b >= a and b >= c:
    if a >= c:
        print(a)
    elif c >= a:
        print(c)

elif c >= a and c >= b:
    if a >= b:
        print(a)
    elif b >= a:
        print(b)