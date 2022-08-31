# Leetcode case
# 122. Best Time to Buy and Sell Stock II

"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
"""

# soution의 3번 해답방식으로 접근, 아쉬운 부분은 내가 생각한 접근 방식이 solution 2인점
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(prices) - 1):

            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]

        return result

# 이코테 실전문제 2
# n=자연수 수, m=숫자가 더해지는 횟수, k=연속 k번을 초과할 수 없음
# 첫줄에 n, m, k가 주어지며 둘째줄에 n개의 자연수가 주어진다

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

def solution_1(nums, n, m, k):
    nums.sort()

    result = 0
    cnt = 0

    while True:
        if m == 0:
            break
        else:
            if cnt == k:
                result += nums[n-2]
                cnt = 0

            else:
                result += nums[n-1]
                cnt += 1

        m -= 1

    return result

# 반복되는 패턴을 파악해 푸는 방법
def solution_2(nums, n, m, k):
    nums.sort()
    first = nums[n-1]
    second = nums[n-2]

    count = int(m/(k+1))*k
    count += m % (k+1)

    result = 0
    result += count * first
    result += (m-count) * second

    return result

# 이코테 실전문제 3
n,m = map(int, input().split())
cards = list()
result = set()
for i in range(n):
  cards.append(list(map(int, input().split())))
  result.add(min(cards[i]))

print(max(result))

# 이코테 실전문제 4
n, k = map(int, input().split())

def solution_1(n, k):

    cnt = 0
    while True:
        if n == 1:
            break
        else:
            if n % k != 0:
                n -= 1
                cnt += 1
            else:
                n /= k
                cnt += 1

    return cnt