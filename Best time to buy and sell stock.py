def maxProfit(prices):
    
    min_price = float('inf')  # Set to infinity at the start, so any price will be lower
    max_profit = 0  # Initialize maximum profit to 0

    # Loop through the list of prices
    for price in prices:
        # Update the minimum price encountered so far
        if price < min_price:
            min_price = price
        # Calculate the profit if selling on the current day
        profit = price - min_price
        # Update the maximum profit if the current profit is higher
        if profit > max_profit:
            max_profit = profit

    return max_profit

# Example usage:
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5