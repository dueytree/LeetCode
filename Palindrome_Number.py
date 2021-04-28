# Palindrome Number
# https://leetcode.com/problems/palindrome-number/

# 숫자를 뒤집었을 때, 121 처럼 본 숫자와 같은 것을 Palindrome Number 라고 한다.
# 보기와 같이 음수는 뒤집었을 때 본 숫자와 맞지 않는다.
# 간단하게 입력받은 int: x 값을 문자열로 덮어주고, bool: 형식으로 기본 코드를 제공함에 따라
# 바로 return 해서 리스트 뒤집기를 이용해 뒤집어 true와 false를 출력한다.

def Palindrome(x):
    return str(x) == str(x)[::-1]

def test_solution():
    assert Palindrome(121) == True
    assert Palindrome(-121) == False
    assert Palindrome(10) == False
    assert Palindrome(-101) == False