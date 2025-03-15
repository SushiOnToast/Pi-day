import random

inside = 0
total = 1700000  # More dots = better accuracy!

for _ in range(total):
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        inside += 1

pi_estimate = (inside / total) * 4
print("Estimated Pi:", pi_estimate)
