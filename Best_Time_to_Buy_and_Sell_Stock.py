# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# 입력받은 리스트의 순서가 주식의 값이고, 그 순서대로 차익을 계산했을 때 가장 큰 수익을 내는 시점을 파악하는 문제이다.
# 가장적을때 사야하며, 사고나서 가장높을 때 팔아야한다. 단순하게 brute force로 문제를 풀었다.
# for문이 두개 돌아가며 시간초과로 오답이다.
# 이 문제는 저점과 현재값과의 차이 계산으로 풀이를 해야한다.
# 현재값을 가르키는 포인트가 오른쪽으로 이동하면서 이전 상태의 저점을 기준으로 가격차이를 계산하고,
# 만약 클 경우 최댓값을 계속 바꿔 나가는 방식으로 풀어야 한다.
# 먼저 마지막에 이익을 출력해줄 변수 profit을 설정하고 가장 높은 값을 min_price에 넣어준다.
# 가장 높은 값을 넣어주는 이유는 어떤값이 들어오든 바로 교체될 수 있게 하게끔이다.
# import sys를 넣어주고, sys.maxsize를 min_price에 넣고 입력된 prices를 반복문을 돌려 최솟값과 최댓값을
# 계속 갱신시켜준다. 반복문이 끝나면 가장 큰 이익이 들어있는 profit을 return 한다.

import sys

def maxProfit(prices):
    profit = 0
    min_price = sys.maxsize
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit

def test_solution():
    assert maxProfit([7,1,5,3,6,4]) == 5
    assert maxProfit([7,6,4,3,1]) == 0

# brute force (시간초과)
# def maxProfit(prices):
#     answer = 0
#     for i, price in enumerate(prices):
#         for j in range(i, len(prices)):
#             answer = max(prices[j] - price, answer)
#     return answer
#
# print(maxProfit([7,1,5,3,6,4]))