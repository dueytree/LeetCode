# Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/

# 리스트 nums의 값을 누적 합산을 통해 리스트로 출력시켜주는 문제이다. 간단하게 반복문 한개로 풀이했다.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        strg = 0
        for element in nums:
            strg += element
            answer.append(strg)
        return answer

