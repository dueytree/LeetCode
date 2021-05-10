# Arr Partition 1
# https://leetcode.com/problems/array-partition-i/

# 문제를 잘 읽어보면 생각보다 간단하다. 변수와 빈 리스트 설정 후 for문과 if문으로 쉽게 문제를 해결할 수 있다.
# 입력받은 리스트를 sort정렬한 후 변수와 빈 리스트를 지정한 다음 반복문을 돌려 오름차순으로 합 계산을 진행 한 후
# 합을 담은 값을 return 한다.
# 이 문제는 잘 보면 0부터 시작하여 짝수번째 수가 min(a, b) 로 보았을 때 항상 작은 값이 위치하고 있다.
# 간단히 슬라이싱으로 [::2] 두칸씩 건너 뛰는 방법을 통해 쉽게 풀이할 수 있다.

def arrayPairSum(nums):
    return sum(sorted(nums)[::2])

def test_solution():
    assert arrayPairSum([1, 4, 3, 2]) == 4
    assert arrayPairSum([6, 2, 6, 5, 1, 2]) == 9