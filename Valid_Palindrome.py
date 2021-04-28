# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

#

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