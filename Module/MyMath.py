pi = 3.14

def oneAddN(end):   #1부터 N까지의 합을 구해주는 함수
    sum = 0
    for i in range(end):
        sum =+ i+1
    return sum

def oneMulN(end):   #1부터 N까지의 곱을 구해주는 함수
    total = 1
    for i in range(end):
        total *= i+1
    return total

if __name__ == '__main__':
    print('math 모듈 실행')
    print(__name__)

print('math 모듈 실행')
print(__name__)