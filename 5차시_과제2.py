def sum_between(start, end):
    if start > end:  # start가 end보다 클 경우 처리
        print("start는 end보다 클 수 없습니다.")
        return 0  # 더 이상 진행하지 않고 0을 반환
    result = 0
    for i in range(start, end + 1):  # start부터 end까지 반복
        result += i
    return result

print("0 ~ 10: ", sum_between(0, 10))
print("0 ~ 100: ", sum_between(0, 100))
print("50 ~ 100: ", sum_between(50, 100))
print("30 ~ 10: ", sum_between(30, 10))
