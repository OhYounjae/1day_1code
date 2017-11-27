n = int(input())
a = list(map(int, input().split()))
m = 0
score = []
sum_all = 0

for i in range(len(a)):
    if a[i] >= m:
        m = a[i]

for j in range(len(a)):
    score.append(a[j]/m*100)

for k in range(len(score)):
    sum_all += score[k]

#자연수로 나눠떨어질때는 소수점 셋째자리에서 반올림 해줄 수가 없어서 round()을 쓰면 안된다.
# %.2f 를 사용해서 소수 둘째자리까지 해결해준다.
print("%.2f" %(sum_all/n))


"""
#이건 친구가 보내준 코드
#마지막 줄에서 깨달음을 얻음
n = int(input())
score = list(map(int, input().split()))

max = max(score)

after_score = list(map(lambda x: round(x / max * 100, 3), score))
print("%.2f" %(sum(after_score) / n))

"""