#brute force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print(prices)
        profit = 0
        for i in range(0,len(prices)):
            for j in range(i,len(prices)):
                currentprofit = prices[j]-prices[i]
                print("i value = ",prices[i] , "j value = ",prices[j] , "profit = ", currentprofit)
                if currentprofit > profit:
                    profit = currentprofit
                    print("profit updated to ", profit)
        return profit

#optimal
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print("[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
        print(prices)
        profit = 0
        l = 0
        r = 1
        print(len(prices))
        while r < len(prices):
            dif = prices[r] - prices[l]
            print("analizing at l = ",l," and r = ",r)
            print(prices[r]," - ",prices[l]," = ", dif)
            if dif < 0:
                print("value is negative, change pointers")
                l = r
                r = l + 1
                print("new pointers l = ",l," and r = ",r)
            else:
                if dif > profit:
                    print("new profit of ", dif)
                    profit = dif
                r = r + 1
            print("  ")
        print("break at l = ",l," and r = ",r)
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1
        while r < len(prices):
            dif = prices[r] - prices[l]
            if dif < 0:
                l = r
                r = l + 1
            else:
                if dif > profit:
                    profit = dif
                r = r + 1
        return profit