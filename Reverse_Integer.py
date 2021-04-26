# Reverse Integer
# https://leetcode.com/problems/reverse-integer/

# 이 문제는 단순히 정수를 뒤집어주면 되는 문제인데, 조건이 있다. 32비트 정수일 때만 정상 return 해야하고,
# 그 범위를 벗어나게 될 경우 뒤집어진 정수가 아니라 0을 return 해야한다.
# 일단 뒤집어진 리스트 넣어줄 변수를 만들어 주고, abs() 함수를 사용해 절대값으로 리스트에 넣어준다.
# 그리고 음수의 조건과 32비트-64비트 조건을 넣어준다.

def reverse(s):
    rev_list = int(''.join(_ for _ in list((str(abs(s))))[::-1]))
    if s < 0:
        rev_list = rev_list * (-1)
    if ((-(2 ** 31)) > rev_list) or (rev_list > (2 ** 31)- 1):
        return 0
    return rev_list

def test_solution():
    assert reverse(123) == 321
    assert reverse(-123) == -321
    assert reverse(120) == 21
    assert reverse(0) == 0