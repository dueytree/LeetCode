# Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# 문제를 보면 연결된 리스트를 문자열로 이어 붙인 다음에 숫자로 변환하고
# 모두 계산한 다음 다시 연결 리스트로 바꾸면 쉽게 풀이할 수 있을 것 같았다.
# 풀이는 어렵지 않으나 역순으로 리스트를 두번 뒤집어야하기 때문에 소요 시간이 어느정도 예상되었다.
# 일단 연결 리스트를 뒤집어 계산할 수를 준비하고, 연결 리스트를 파이썬 리스트로 변환 시켜 준 다음(덧셈 계산을 위해)
# 그리고 node를 반복해 값을 리스트에 추가하는 함수를 넣어준다. 그리고 마지막으로 덧셈 연산을 진행하는 함수를 넣어주고
# 계산이 끝난 결과를 연결 리스트로 바꿔 변환해 마지막 문자열로 감싸주는 것까지 해주며 return한다.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    def toList(self, node: ListNode) -> ListNode:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    def toReverseLinkedList(self, result: ListNode) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))

        return self.toReverseLinkedList(str(resultStr))