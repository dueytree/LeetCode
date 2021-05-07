# 3 Sum
# https://leetcode.com/problems/3sum/

# 이 문제는 3개의 수를 합해 0이 나오는 모든 경우를 찾는 문제이다.
# brute force로 반복문 3개와 if문으로 진행할경우 시간복잡도가 n세제곱으로 시간초과가 나올 수 있다.
# 이번 문제도 투포인터 방식으로 양 끝에서 같이 진행하는 것이 좋겠다고 판단했다.
# 일단 첫번째 입력받을 리스트는 정렬이 되어있지않아 sort정렬을 해주고, 마지막에 출력해줄
# answer 빈 리스트를 설정한다. 그리고 리스트에서 -1의 값이 2개이므로 중복된 값이 나올 수 있다.
# 그래서 중복값을 제외할 식을 넣어주고, 건너뛰게끔 continue를 넣어준다.
# 이후에 left와 right 값을 정해주고, 간격을 좁히면서 합을 계산해 주는 부분을 구성한다.
# 계산한 이후 조건문을 통해 합이 0보다 작으면 왼쪽에서 한칸, 크면 오른쪽에서 한칸 움직이며 합이 0과 같을때 까지
# 이동하며 반복한다. 그리고 답이 나와 answer에 append 해주고 동일한 값 중복을 생각해 left, right 값을
# +=1, -=1 해준다.

def threeSum(nums):
    answer = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                answer.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return answer

def test_solution():
    assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert threeSum([]) == []
    assert threeSum([0]) == []