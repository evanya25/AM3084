import numpy as np
import matplotlib.pyplot as plt

h = [5, 2, 8, 4, 7, 1, 5, 10, 4, 7,
     3, 6, 3, 5, 2, 7, 4, 9, 5, 11]

print("Mean =", np.mean(h))
print("Median =", np.median(h))
print("Variance =", np.var(h, ddof=1))
print("Standard deviation =", np.std(h, ddof=1))

# Change 8 to 12
h[2] = 12

print("\nAfter changing 8 to 12")
print("Mean =", np.mean(h))
print("Median =", np.median(h))
print("Variance =", np.var(h, ddof=1))
print("Standard deviation =", np.std(h, ddof=1))

plt.hist(h, edgecolor="black")
plt.xlabel("Study hours")
plt.ylabel("Frequency")
plt.show()