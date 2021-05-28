# Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/

# 문제 의도에서 큐를 스택으로 만들어보라고 한다.
# 일단 큐를 deque로 선언하고 문제 의도대로 큐의 연산을 사용해 구현해야한다. 복잡하지만 값을 삽입한 후에 직전 삽입한
# 값을 맨 앞에 두는 상태로 전체를 재정렬 해준다. 이렇게 되면 큐에서 맨 앞의 값을 꺼낼때 스택처럼 가장 먼저 삽입한 값이
# 나오게 된다. 이렇게 될때 복잡도는 n이다.

import collections
class MyStack:
    def __init__(self):
        self.q = collections.deque()
    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0