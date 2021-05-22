# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

# 기본적인 stack 문제로, 빈 리스트 stack을 만들어 주고, table 딕셔너리에 값을 넣어준 뒤
# for문 안에 조건문을 돌려 pop를 사용해 마지막에 boolean 값으로 return 해준다.

def isValid(self, s: str) -> bool:
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0