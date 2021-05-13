# 1단계. 리스트에 들어있는 각 자연수의 개수를 셉니다.

arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
count = [0] * 4

for x in arr:
    count[x] += 1

print(f"1의 갯수 : {count[1]}")
print(f"2의 갯수 : {count[2]}")
print(f"3의 갯수 : {count[3]}")

# 2단계. 가장 많이 등장하는 수의 개수를 구합니다
counter = [0, 2, 3, 5]

def 최대값(arr):
    large = 0
    for x in arr:
        if x >large:
            large = x
    return large

def 최소값(arr):
    기존값 = 1001
    for x in arr:
        if x < 기존값 and x !=0:
            기존값 = x
    최소 = 기존값
    return 최소

a = 최소값(counter)
print(a)
