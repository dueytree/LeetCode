# Reverse String
# https://leetcode.com/problems/reverse-string/submissions/

# 단순 문자열을 뒤집는 문제이다. reverse 함수로 간단히 뒤집어 주면 된다.
# 두번째 풀이는 reverse 함수를 이용하지 않은 풀이다. 왼쪽, 오른쪽 포인트 하나씩으로 while문을 돌리고,
# 왼쪽 오른쪽 인덱스 값으로 서로를 바꿔주는 방법을 이용한다.

def reverseString(s):
    s.reverse()
    return s


def test_solution():
    assert reverseString(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
    assert reverseString(["H", "a", "n", "n", "a", "h"]) == ["h", "a", "n", "n", "a", "H"]



# def reverseString(s):
#     left, right = 0, len(s) - 1
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
