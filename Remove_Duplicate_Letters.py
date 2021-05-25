# Remove Duplicate Letters
# https://leetcode.com/problems/remove-duplicate-letters/

# 스택에 쌍여있는 문자이면서 뒤에 다시 붙을 분자가 남아 있으면 쌓아둔걸 꺼내고(처리된 문자여부 확인)
# 이미 확인된 문자열을 pop로 지워주는 방식

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            attach = s[s.index(char):]
            if set(s) == set(attach):
                return char + self.removeDuplicateLetters(attach.replace(char, ""))
        return ''


def test_solution():
    assert removeDuplicateLetters("bcabc") == "abc"
    assert removeDuplicateLetters("cbacdcbc") == "acdb"