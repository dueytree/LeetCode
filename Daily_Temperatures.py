# Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

# 온도와 날짜를 그래프처럼 그려주면 이해하기 정말 편하다.
# 현재 시점의 인덱스를 계속 스택에 쌓아주고, 전보다 상승하는 지점에서 현재 온도와 스택의 넣어둔 인덱스의 온도를
# 비교해서 높으면 스택의 값을 pop으로 꺼내주고 현재 인덱스와 스택의 인덱스 차이를 return 해준다.


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, now in enumerate(temperatures):
            while stack and now > temperatures[stack[-1]]:
                last_temp = stack.pop()
                answer[last_temp] = i - last_temp
            stack.append(i)
        return answer