# Two Sum
# https://leetcode.com/problems/two-sum/

# 이 문제는 nums 정수 리스트와 target 정수를 주고, 리스트 인덱스 값의 합으로 target 값을 만드는 문제로
# 답으로 target을 만든 인덱스를 return 해야한다.
# 단순히 쉽게 brute-force로 처음부터 끝까지 계산하여 나타낼 수 있고,
# in enumerate로 모든 조합을 비교하지 않고 첫번째 값을 뺀 값이 존재하는지 여부로 문제를 풀이할 수 있다고 생각했다.


def solution(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# def solution(nums, target):
#     for i, n in enumerate(nums):
#         complement = target - n
#         if complement in nums[i + 1:]:
#             return nums.index(n), nums[i + 1:].index(complement) + (i + 1)


def test_solution():
    assert solution([2, 7, 11, 15], 9) == [0, 1]
    assert solution([3, 2, 4], 6) == [1, 2]
    assert solution([3, 3], 6) == [0, 1]