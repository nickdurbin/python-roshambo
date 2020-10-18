'''
You are given the prices of a stock, in the form of an array of integers, prices. Let's say that prices[i] is the price of the stock on the ith day (0-based index). Assuming that you are allowed to buy and sell the stock only once, your task is to find the maximum possible profit (the difference between the buy and sell prices).

Note: You can assume there are no fees associated with buying or selling the stock.

Example

For prices = [6, 3, 1, 2, 5, 4], the output should be buyAndSellStock(prices) = 4.

It would be most profitable to buy the stock on day 2 and sell it on day 4. Thus, the maximum profit is prices[4] - prices[2] = 5 - 1 = 4.

For prices = [8, 5, 3, 1], the output should be buyAndSellStock(prices) = 0.

Since the value of the stock drops each day, there's no way to make a profit from selling it. Hence, the maximum profit is 0.

For prices = [3, 100, 1, 97], the output should be buyAndSellStock(prices) = 97.

It would be most profitable to buy the stock on day 0 and sell it on day 1. Thus, the maximum profit is prices[1] - prices[0] = 100 - 3 = 97.
'''

"""
Lets try a single pass Linear solution
"""
def second_pass_buyAndSellStocks(prices):
    # O(n)
    # set a min price to 9999999999999 (or max int)
    # set max profit to 0
    # loop over all prices
        # if our prices at the current index are less than the minimum price
            # set our min price to that number
        # otherwise if the prices at the current index minus the min price are greater than the max profit
            # set the max profit to that number
    # return the max profit
    pass

def buyAndSellStock(prices):
  # Create a variable to store our profit or greatest difference
  max_profit = 0
  min_price = 99999999
  for i in prices:
    if i <= min_price:
      min_price = i
    elif i - min_price > max_profit:
      max_profit = i - min_price
  return max_profit

"""
 let's do a first pass naive brute force solution
"""
prices = [6, 3, 1, 2, 5, 4]
def first_pass_buyAndSellStocks(prices):
    # O(n^2)
    # track max profit
    # loop over the prices
        # loop over prices + 1
            # set a current profit prices at j - prices at i
            # check if the current profit is greater than the max profit
                # set our max profit to the current profit
    # return our max profit
    pass
# test

prices = [6, 3, 1, 2, 5, 4]
print(buyAndSellStock(prices)) # => 4
# print(second_pass_buyAndSellStocks(prices)) # => 4