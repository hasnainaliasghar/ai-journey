def fixed_point_iteration(seed_value, iterations=15):
    """
    Simulates repeatedly applying f(x) = 1 + 1/x to show convergence
    to the stable fixed point (the Golden Ratio).
    """
    x = seed_value
    print(f"Starting with seed value: {x}")
    print("-" * 35)

    for i in range(1, iterations + 1):
        # Prevent division by zero if x becomes exactly 0
        if x == 0:
            print("Error: Division by zero encountered.")
            break

        x = 1 + 1 / x
        print(f"Iteration {i:2d}: x = {x:.6f}")

    return x


# --- Try different seed values ---

# 1. Starting with a positive number
print("--- Case 1: Positive Seed ---")
fixed_point_iteration(seed_value=1.0)

print("\n--- Case 2: Random Negative Seed ---")
# Even a negative seed close to the unstable fixed point will jump over to 1.618
fixed_point_iteration(seed_value=-0.65)

print("\n--- Case 3: The Unstable Fixed Point ---")
# If you start *exactly* on the unstable fixed point, it stays there
unstable_fixed_point = (1 - 5 ** 0.5) / 2  # Approx -0.618033
fixed_point_iteration(seed_value=unstable_fixed_point)