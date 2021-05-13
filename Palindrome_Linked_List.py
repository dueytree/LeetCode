# Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# 간단히 입력받은 리스트의 값을 팰린드롬인지 아닌지를 판단하는 문제이다.
# 리스트를 pop함수를 사용해 인덱스를 지정해 비교하여 boolean 형태로 출력하면 쉽게 풀 수 있다.
# 일단 입력 리스트에 아무 값이 없을 때 바로 True를 출력해주는 조건문을 넣어주고
# 일반 리스트를 파이썬 리스트로 변환해 주고 마지막에 pop함수를 이용해 팰린드롬 여부를 판단해 준다.

def isPalindrome(head):
    some_list = []
    if not head:
        return True
    strg = head
    while strg is not None:
        some_list.append(strg)
        strg = strg.next
    while len(some_list) < 1:
        if some_list.pop(0) != some_list.pop():
            return False
    return True


def test_solution():
    assert isPalindrome([1, 2, 2, 1]) == True
    assert isPalindrome([1, 2]) == False