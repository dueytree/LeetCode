# Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

# 문제에서 높이와 너비 모든 공간을 모두 체크하게 되면 n제곱의 풀이가 된다. 시간복잡도가 너무 높기때문에
# 필요한 만큼만 확인할 수 있도록 해야한다. 양쪽에서 확인할 수 있는 투포인트 방식으로 문제를 풀이했다.
# 가장 높은 막대를 확인해서 왼쪽과 오른쪽을 가리는 장벽이다. 부피에 영향은 없으며 그 부분을 포인트로 정해
# 왼쪽과 오른쪽을 나누고, 가장 큰 높이의 막대까지 왼쪽에서 오른쪽까지의 변수가 현재 높이와의 차이만큼 물 높이 변수를
# 증가시켜준다. 이때 왼쪽이든 오른쪽이든 그만큼 낮은 쪽이 가장 큰 막대로 증가하며 다가서기 때문에, 오른쪽이 크다면
# 왼쪽 += 1, 왼쪽이 크다면 오른쪽 += 1 해주며 반복해서 가장 높이가 큰 막대에 도달할 때 좌우 포인터가 만나 n의 시간복잡도를
# 보여주며 답을 return하게 된다.

def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    volume = 0
    while left < right:
        left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
        if height[left] <= height[right]:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume

def test_solution():
    assert trap([4, 2, 0, 3, 2, 5]) == 9