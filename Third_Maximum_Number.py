# Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/

# 리스트에서 3번째로 큰 수를 찾는 문제인데, 간단하다
# nums 리스트에 set함수로 중복값을 제거해주고 내림차순으로 정렬한 뒤
# 리스트 안에 수가 3개보다 적을때를 생각해 조건문을 넣어주면 된다.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = sorted(nums, reverse=True)
        if len(nums) < 3:
            answer = nums[0]
        else:
            answer = nums[2]
        return answer