# Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

# 홀수 노드 뒤에 짝수 노드가 와야함으로 홀, 짝수 노드를 구성한 다음 홀수 노드의 마지막 뒤에 짝수 노드의 처음을
# 이어준다. 홀수 변수는 head, 짝수 변수는 head.next이다. 짝수 변수가 즉 짝수의 헤드로
# even_head = even = head.next 로 일단 시작한다.
# while 반복문을 태워주고 다중할당으로 홀짝 처리를 하나로 묶어 처리한다.

def oddEvenList(self, head: ListNode) -> ListNode:
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head
    return head

def test_solution():
    assert oddEvenList([1,2,3,4,5]) == [1,3,5,2,4]
    assert oddEvenList([2,1,3,5,6,4,7]) == [2,3,6,7,1,5,4]