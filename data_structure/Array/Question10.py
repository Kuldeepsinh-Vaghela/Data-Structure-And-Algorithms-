#  Question 10
#  leet code 121: Best Time to Buy and Sell Stock
#  You are given an array prices where prices[i] is the price of a given stock on the ith day
#  You want to maximize your profit by choosing a single day to buy one stock and choosing a \
#  different day in the future to sell that stock.
#  Return the maximum profit you can achieve from this transaction. If you cannot achieve any \
#  profit, return 0.

def maxProfit(prices):
        min_value_indx = 0
        max_value_indx = 1
        profit1 = []
        while max_value_indx <= len(prices)-1:
            min_value = prices[min_value_indx]
            max_value = prices[max_value_indx]
            if min_value > max_value:
                min_value_indx += 1
                max_value_indx = min_value_indx+ 1
            elif min_value == max_value:
                min_value_indx += 1
                max_value_indx = min_value_indx+1
            else:
                profit2 = max_value-min_value
                profit1.append(profit2)
                max_value_indx += 1
        if profit1 == []:
            return 0
        else:
            return max(profit1)

# Use Case: 1
# prices = [7,1,5,3,6,4]
# Output = 5
# Expected = 5

# Use Case: 2
# prices = [7,6,4,3,1]
# Output = 0
# Expected = 0