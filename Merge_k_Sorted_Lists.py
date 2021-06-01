# Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# 대부분의 우선순위 큐 문제를 풀 때 heapq 모듈을 사용한다. 근데 입력받은 리스트로 문제를 풀게 되면
# 작은 순서대로 pop할 수 있게 된다. 하지만 이렇게 될때 ListNode에서 중복된 값을 넣을 수 없다고 오류가 발생한다.
# 오류를 피하기 위해 연결 리스트의 순서를 맞춰 반복문으로 삽입한다. 이 후에 heappop로 값을 추출하고, 결과값이 될
# 노드 result에 하나씩 추가해준다. 그리고 추출한 연결 리스트의 next 노드는 while문을 사용해 heappop를 사용해
# 값이 남지 않을때 까지 반복해주면 result값에 작은값의 노드부터 차례대로 채워지게 된다.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next