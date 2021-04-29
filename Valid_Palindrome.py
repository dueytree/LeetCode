# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

# 이 문제는 문자열을 직접 입력받아 팰린드롬을 판별한다. 빈문자열을 만들고 반복문을 돌려 isalnum 함수를 이용해
# 영문자, 숫자만을 대상으로 판별하는 함수를 사용해 조건문을 걸어주고, 그 값을 대문자는 소문자로 바꿔주어 append 해준다.
# 이후 while 반복문으로 하나씩 제거해 나가며 boolean 형태로 return 해준다.

def isPalindrome(s) -> bool:
    strs= []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True

def test_solution():
    assert isPalindrome("A man, a plan, a canal: Panama") == True
    assert isPalindrome("race a car") == False