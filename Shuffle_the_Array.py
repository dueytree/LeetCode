# Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/

# 입력받은 nums의 리스트 값을 x, y 인덱스로 생각해봤을때, nums의 총 인덱스 길이를
# 반으로 나눈 뒤, 반복문을 통해 x1, y1, x2,y2 형식의 배열로 빈 리스트에 append해준다.

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        for i in range(len(nums) // 2):
            answer.append(nums[i])
            answer.append(nums[i + n])
        return answer