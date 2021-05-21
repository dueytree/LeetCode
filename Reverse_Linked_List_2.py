# Reverse Linked List 2
# https://leetcode.com/problems/reverse-linked-list-ii/

# 앞서 풀었던 문제들과 같이, 반복구조로 문제를 풀이해야한다. 단순한 내장함수로 답을 낼 수 있지만
# 문제의도에 맞춰 Reverse Linked List 1의 방식에 맞춰 반복구조를 통해 스왑하는 형식으로 문제를 풀이한다.
# 일단 받은 리스트와 인덱스 기준 값을 보고 시작 값과 끝 값을 지정한 뒤 반복문을 통해 노드들을 차례대로 뒤집어 준다.
# 사실 반복구조로 노드를 변경하는 문제를 풀때 굉장히 값이 헷갈려 잘못보는 경우가 많다.
# 요점을 잘 확인하고 판단해서 문제를 풀어야 한다.
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head
        for _ in range(left - 1):
            start = start.next
        end = start.next

        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next
