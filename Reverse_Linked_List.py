# Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# 전에 풀었던 문제와 비슷하다. 입력받은 연결 리스트를 뒤집어서 출력해야하는 문제인데, 마찬가지로 반복되는 구조로
# 문제를 해결할 수 있다. 이전값과 현재값을 넣어줄 리스트를 만들어 주고, 입력받은 리스트 만큼 while문을 사용한다.
# 다음값과 이전값의 최신화를 재귀적으로 반복하여 current 끝까지 돌고, 이전값을 return 하는 방식이다.

def reverseList(head):
    prev, current = None, head
    while current:
        next, current.next = current.next, prev
        prev, current = current, next
    return prev

def test_solution():
    assert reverseList([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverseList([1, 2]) == [2, 1]