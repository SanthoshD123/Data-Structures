def coin_change(coins, amount):
    # Sort coins in descending order
    coins.sort(reverse=True)
    
    # Initialize the count of coins
    coin_count = 0
    
    # Iterate through the coins
    for coin in coins:
        if amount == 0:
            break
        # Find the maximum number of coins of this denomination
        count = amount // coin
        coin_count += count
        amount -= count * coin
    
    # If we have successfully given the exact amount, return the coin count
    if amount == 0:
        return coin_count
    else:
        return -1  # Return -1 if it's not possible to make the exact amount

# Example usage
coins = [1, 5, 10, 25]
amount = 63
result = coin_change(coins, amount)
print(f"Minimum number of coins for amount {amount}: {result}")
