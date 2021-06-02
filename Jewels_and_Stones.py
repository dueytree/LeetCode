# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

# 단순하게 돌의 갯수를 구해놓고, 보석을 키로 가지는 개수를 합산하여 count값을 구할 수 있다.
# 돌의 요소를 한 문자씩 쪼개서 반복한다. 처음 만나는 문자면 1, 있던 문자면 1을 더해준다. 이 값이 dics에 저장되고
# 각 문자별 빈도 수가 저장되며 이제 보석의 문자를 다시 반복문을 통해 그 해당 문자의 빈도 수를 더해주면
# count값을 구할 수 있다.

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dics = {}
        count = 0

        for element in stones:
            if element not in dics:
                dics[element] = 1
            else:
                dics[element] += 1

        for char in jewels:
            if char in dics:
                count += dics[char]
        return count