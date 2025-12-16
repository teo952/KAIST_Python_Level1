def count_list(lst):
    odd_num = 0  # 홀수 개수
    even_num = 0  # 짝수 개수

    for num in lst:  # 리스트의 요소를 하나씩 반복
        if num % 2 == 1:  # 홀수라면
            odd_num += 1
        else:  # 짝수라면
            even_num += 1

    return odd_num, even_num

print(count_list([1, 4, 7, 9, 12, 14, 17, 25]))
