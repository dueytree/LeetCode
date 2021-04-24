# Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

# 문제 자체가 한 시점으로 비교를 시작하게 되면 실행속도가 굉장히 늦다. 그래서 중앙부를 기점으로 두 시점으로 동시에
# 비교를 진행해 비교적 빠른 실행속도를 보이도록 하는 것이 중요하다.
# 두 시점을 앞에서부터 각 2칸, 3칸으로 비교를 시작하고, 입력받은 문자열이 팰린드롬인 경우 그 자리에서 정지,
# 두 시점으로 확장해가는 방식으로 진행하며, 홀수와 짝수 모든 경우에 판별한다.
# 모든 경우를 판별하는 과정에서 많은 시간이 소요되므로 짝수와 홀수를 필터링 하는 걸로도 시간 단축이 크기 때문에
# 넣어준다. 답을 넣어줄 answer 빈 문자열을 만들어 주고, 반복문을 통해 answer값에 중첩함수로 계산되는 두 시점과, answer값, key값 중
# 가장 큰값을 answer값으로 넣어준 뒤 마지막에 return 한다.
# 두 시점을 가리키는 expand함수는 왼쪽 오른쪽의 조건과 문자열 s의 왼쪽, 오른쪽 값을 넣은 인덱스를 비교하고
# 왼쪽값과 오른쪽값의 인덱스를 추가해주며 모든 경우를 판별한다.

def longestPalindrome(s):
    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1:right - 1]

    if len(s) < 2 or s == s[::-1]:
        return s
    answer = ''
    for i in range(len(s) - 1):
        answer = max(answer,
                        expand(i, i + 1),
                        expand(i, i + 2),
                        key=len)
    return answer


def test_solution():
    assert longestPalindrome("babad") == "bab"
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("a") == "a"
    assert longestPalindrome("ac") == "a"