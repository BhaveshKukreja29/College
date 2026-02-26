import random

def objective(x):
    return -(x * x) + 4 * x + 10

def hill_climbing(start, step_size, max_iter):
    current = start
    current_val = objective(current)

    for i in range(max_iter):
        left = current - step_size
        right = current + step_size

        left_val = objective(left)
        right_val = objective(right)

        if left_val > current_val and left_val >= right_val:
            current = left
            current_val = left_val
        elif right_val > current_val:
            current = right
            current_val = right_val
        else:
            print("Stuck at local optimum, iteration:", i)
            break

        print(f"Step {i}: x = {current:.4f}, f(x) = {current_val:.4f}")

    return current, current_val

start = random.uniform(-10, 10)
step_size = 0.1
max_iter = 1000

print(f"Starting point: x = {start:.4f}")
best_x, best_val = hill_climbing(start, step_size, max_iter)
print(f"\nBest solution: x = {best_x:.4f}, f(x) = {best_val:.4f}")
