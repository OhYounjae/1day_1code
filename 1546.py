n = int(input())
a = list(map(int, input().split()))
m = 0
score = []
sum = 0

for i in range(len(a)):
    if a[i] >= m:
        m = a[i]

for j in range(len(a)):
    score.append(a[j]/m*100)

for k in range(len(score)):
    sum += score[k]

print(round(sum/n, 2))