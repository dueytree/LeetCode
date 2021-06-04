# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# 중복없는 최대 문자열의 길이를 구하는 문제이다. 빈 딕셔너리를 만들고, 최대 길이와 시작을 0으로 설정한 뒤,
# 인덱스와 문자를 반복하는 enumerate(s)반복문으로 조건문에 딕셔너리 안에 문자가 있거나 딕셔너리 char가 시작값보다 같거나 클때
# 시작값을 문자 +1 을 넣어준다. else 문에서 최대길이에 최대길이, index - start + 1을 넣어주고 조건문을 나와서
# 딕셔너리[char]에 index 값을 넣어주고 다시 반복한다.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
            used[char] = index
        return max_length