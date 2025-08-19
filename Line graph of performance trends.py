import matplotlib.pyplot as plt

# Data for iterations (1–10)
iterations = list(range(1, 11))
method_a = [55, 60, 65, 68, 72, 75, 78, 80, 82, 84]
method_b = [60, 65, 70, 74, 77, 81, 84, 87, 89, 91]

plt.figure(figsize=(8,6))
plt.plot(iterations, method_a, marker='o', label='Method A', color='blue')
plt.plot(iterations, method_b, marker='s', label='Method B', color='green')

plt.title("Performance Trends", fontsize=14)
plt.xlabel("Iterations", fontsize=12)
plt.ylabel("Accuracy (%)", fontsize=12)
plt.ylim(50, 100)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()

# Save the figure
plt.savefig("Figure_4_2_Performance_Trends.png", dpi=300)
plt.show()
