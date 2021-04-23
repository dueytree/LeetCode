# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# 문자열에서 중복없이 가장 길게 나열된 문자열을 찾는 문제이다. 따라서 사용된 문자열과 그 문자열의 인덱스를 같이 담아줄 수 있게
# 딕셔너리를 하나 만들어 주고, 가장 길게 나열된 문자열의 길이를 담아줄 변수, 현재 위치에서 시작될 변수를 지정하고
# 문자열 index와 문자열 알파벳 하나를 지정하고 enumerate함수를 사용해 튜플 형태로 돌아준다.
# 조건문으로 알파벳이 딕셔너리에 담겨있을때, 동시에 딕셔너리의 알파벳 값이 시작될 현재 위치 값보다 크거나 같을때
# 초기값을 딕셔너리 알파벳 값에 +1 한 값으로 넣어주고
# 조건에 맞지 않을 시 max_length 값에 max_length와 index - start + 1 한 값 중에 큰 값을 넣어준다.
# 조건문이 통과되고 사용된 알파벳값에 index를 넣어주고 다시 반복문을 시작한다.
# 이 과정이 지나 딕셔너리안에 가장 긴 문자열이 넣어지고 반복문이 모두 돌아 끝나면 max_length 값을 return해 답을 구한다.

def lengthOfLongestSubstring(s):
    used_char = {}
    max_length = 0
    start = 0
    for index, char in enumerate(s):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            max_length = max(max_length, index - start + 1)
        used_char[char] = index
    return max_length


def test_solution():
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3