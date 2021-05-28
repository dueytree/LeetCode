# Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/

# 반대로 큐를 스택으로 나타내는 문제다. 스택을 큐로 표현할때는 맨 앞의 값부터 꺼냈다면 이번엔 맨 뒤에서 꺼내야한다.
# 이렇게 되면 무한반복이 진행되고 이 때문에 스택을 하나 더 필요하다. 문제에서 얘기했던 것처럼 pop을 사용할때 peek을 호출해
# 재입력하게 되는 방법으로 진행해야한다.
# 이렇게 구현 할때 output의 값이 모두 pop되기 전까지 다시 재입력이 이뤄지지 않기 때문에
# 시간복잡도는 (1)이다.

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []
