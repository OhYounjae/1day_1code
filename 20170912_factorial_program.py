#Kookmin University
#Major: Software
#20171651 오윤재
# 펙토리얼 출력하기

n = int(input('숫자를 입력하시오'))

while n < 0:
    sum = 1
    if n > 0:
        for i in range(1, n+1):
            sum *= i

        print(sum)
        break

    break
