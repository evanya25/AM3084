import numpy as np
import matplotlib.pyplot as plt

# Given data
hours = [5, 2, 8, 4, 7, 1, 5, 10, 4, 7,
         3, 6, 3, 5, 2, 7, 4, 9, 5, 11]

# Calculate original statistics
print("Original Data")
print("Mean:", np.mean(hours))
print("Median:", np.median(hours))
print("Sample Variance:", np.var(hours, ddof=1))
print("Sample Standard Deviation:", np.std(hours, ddof=1))

# Change the first 8 to 12
updated_hours = hours.copy()
updated_hours[2] = 12

# Calculate updated statistics
print("\nUpdated Data")
print("Mean:", np.mean(updated_hours))
print("Median:", np.median(updated_hours))
print("Sample Variance:", np.var(updated_hours, ddof=1))
print("Sample Standard Deviation:", np.std(updated_hours, ddof=1))

# Draw histogram
plt.hist(updated_hours, bins=range(1, 14),edgecolor="black")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.title("Histogram of Updated Study Hours")
plt.show()
