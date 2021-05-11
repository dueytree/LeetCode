# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

# 이 문제는 array[i] 자기 자신을 제외한 나머지 요소의 곱 결과가 되도록 만들어야 한다.
# 근데 조건으로 나눗셈을 하지않고 O(n)으로 문제풀이를 해야한다.
# 애초에 풀이 시작을 자기 자신을 제외하고 왼쪽값의 곱셈결과와 오른쪽값의 곱셈결과를 곱해야 한다.
# 먼저 빈리스트와 n = 1값을 주고, 반복문으로 0부터 nums길이만큼 돌려 answer 값에 n값을 넣어주고
# n 값을 n * nums[i] 로 바꿔준다, 반복문이 끝나면 왼쪽값이 answer에 넣어지고,
# 다시 n값을 1로 초기화 한다음 새로운 반복문으로 왼쪽 곱셈 반복문에서 진행했던 것과 같은 맥락으로
# 왼쪽 곱셈값에 오른쪽 곱셈값을 순서대로 곱해 담은 answer 리스트를 return 한다.

def productExceptSelf(nums):
    answer = []
    n = 1
    for i in range(0, len(nums)):
        answer.append(n)
        n = n * nums[i]

    n = 1
    for i in range(len(nums) - 1, 0 - 1, -1):
        answer[i] = answer[i] * n
        n = n * nums[i]
    return answer

def test_solution():
    assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]