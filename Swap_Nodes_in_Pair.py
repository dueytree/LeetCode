# Swap Nodes in Pair
# https://leetcode.com/problems/swap-nodes-in-pairs/

# 전체 연결 리스트를 순회할 포인트 p를 잡고 그 값에 head.next 값을 넣어준다. head.next 값으로는 재귀호출로
# p.next값을 넣어준 뒤 그 다음엔 p.next값에 head 값을 넣어준다.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head