'''class Solution:
    def maxProfit(self, prices):
        ans = 0

        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] >0:
                ans = ans + (prices[i] - prices[i - 1])
        return ans
obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))
'''

p = [7, 5, 3, 6, 4]
ans = 0
for i in range(1, len(p)):
    if p[i]-p[i-1]>0:
        ans = ans + (p[i]-p[i-1])

print(ans)