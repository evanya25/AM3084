import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Data = pd.read_csv("student_performance.csv")
print(Data)

# Question a
print("Dimension =", Data.shape)
print(Data.dtypes)
print(Data.head())
print(Data.describe())

# Question b
print("Mean in marks =", Data["Exam"].mean())
print("Median in marks =", Data["Exam"].median())
print("Standard deviation in marks =", Data["Exam"].std())

# Question c
print("Correlation =", Data["Study Hours"].corr(Data["Exam"]))

# Question d

plt.figure(figsize=(12, 10)) #12inch wide 10 inch tall
plt.subplot(2,2,1)
plt.scatter(Data["Study Hours"],Data["Exam"])
plt.xlabel("Study Hours")
plt.ylabel("Exam Marks")
plt.title("Study Hours vs Exam Marks")

plt.subplot(2,2,2)
plt.hist(Data["Exam"],bins=10,edgecolor="black")
plt.xlabel("Exam Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Exam Marks")


plt.subplot(2,2,3)
plt.boxplot(Data["Exam"].dropna())
plt.ylabel("Exam Marks")
plt.title("Box Plot of Exam Marks")


plt.subplot(2,2,4)
heatmap_data = Data[['Study Hours', 'Assignment']]
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt='.1f')
plt.title("Heatmap of Study Hours vs Assignment Marks")
plt.show()

