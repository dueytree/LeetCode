# Merge_Two_Sorted_Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# 두개의 리스트를 하나의 리스트로 모은 뒤 정렬해서 출력하는 문제다.
# 단순히 두 리스트를 더해 빈 리스트에 모아서 sort 정렬하면 간단하지만 각 리스트가 listnode로 입력 받게 되므로
# 리스트를 받아와서 두 리스트 중 작은 값이 왼쪽으로 오게 하고, next로 그 다음 값이 붙게하도록 문제를 재귀적으로 풀어줘야한다.
# 조건문에서 비교할 때 수식이 꼬일 수 있으므로 꼭 우선순위가 가장 높은 괄호를 사용하고,
# 두 리스트를 스왑한다. l1에 작은 값을 넣어줬기 때문에 그 다음 값으로 l2를 넣어주고 l1을 return함으로 문제를 풀이한다.

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1

def test_solution():
    assert mergeTwoLists([1,2,4], [1,3,4])
    assert mergeTwoLists([], [])
    assert mergeTwoLists([], [0])