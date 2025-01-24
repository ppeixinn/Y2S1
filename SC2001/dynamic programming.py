def max_profit_2d(C, weights, profits):
    n = len(weights)
    # Initialize a 2D DP array to store max profit for each capacity up to C and up to each item
    dp = [[0] * n for _ in range(C + 1)]

    # Fill the DP table
    for i in range(n):
        for capacity in range(1, C + 1):
            # Option 1: Exclude the item
            dp[capacity][i] = dp[capacity][i - 1] if i > 0 else 0
            
            # Option 2: Include the item (if capacity allows)
            if weights[i] <= capacity:
                dp[capacity][i] = max(dp[capacity][i],dp[capacity - weights[i]][i] + profits[i])

    # Print the DP table with labels
    print("DP Table (Capacity x Items):")
    print("     ", end="")
    for j in range(n):
        print(f"Obj {j} ", end=" ")
    print()
    print("     ", "-" * (5 * n))

    for capacity in range(C + 1):
        print(f"C={capacity:2} |", end=" ")
        for i in range(n):
            print(f"{dp[capacity][i]:4}", end=" ")
        print()
    
    # The maximum profit with the given capacity and all items is in dp[C][n-1]
    return dp[C][n - 1]

# Get user input
try:
    C = int(input("Enter the knapsack capacity: "))
    n = int(input("Enter the number of items: "))

    weights = []
    profits = []
    for i in range(n):
        w = int(input(f"Enter weight of item {i + 1}: "))
        p = int(input(f"Enter profit of item {i + 1}: "))
        weights.append(w)
        profits.append(p)

    # Execute and print the result
    print(f"Maximum profit for P({C}) with weights {weights} and profits {profits} is:", max_profit_2d(C, weights, profits))

except ValueError:
    print("Please enter valid integer values for capacities, weights, and profits.")


"""def max_profit(C, weights, profits):
    n = len(weights)
    # Initialize a 2D DP array to store max profit for each capacity up to C and up to each item
    dp = [[0] * n for _ in range(C + 1)]

    # Fill the DP table
    for i in range(n):
        for capacity in range(1, C + 1):
            # Option 1: Exclude the item
            dp[capacity][i] = dp[capacity][i - 1] if i > 0 else 0
            
            # Option 2: Include the item (if capacity allows)
            if weights[i] <= capacity:
                dp[capacity][i] = max(dp[capacity][i],dp[capacity - weights[i]][i] + profits[i])

    # Print the DP table with labels
    print("DP Table (Capacity x Items):")
    print("     ", end="")
    for j in range(n):
        print(f"Obj {j+1} ", end=" ")
    print()
    print("     ", "-" * (5 * n))

    for capacity in range(C + 1):
        print(f"C={capacity:2} |", end=" ")
        for i in range(n):
            print(f"{dp[capacity][i]:4}", end=" ")
        print()
    
    # The maximum profit with the given capacity and all items is in dp[C][n-1]
    return dp[C][n - 1]

# Given data for test
C = 14
weights = [4, 6, 8]
profits = [7, 6, 9]
print("Maximum profit for P(14) with weights [4, 6, 8] and profits [7, 6, 9] is:", max_profit(C, weights, profits))

weights = [5, 6, 8]
profits = [7, 6, 9]
print("Maximum profit for P(14) with weights [5, 6, 8] and profits [7, 6, 9] is:", max_profit(C, weights, profits))"""
