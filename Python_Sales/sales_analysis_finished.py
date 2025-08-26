# ✅ Sales Analysis Finished Script

# Step 1. Load the Data
with open("sales.txt", "r") as file:
    sales = [int(line.strip()) for line in file]

print(sales)

# Step 2. Basic Math
print("Total Sales:", sum(sales))
print("Average Sale:", sum(sales) / len(sales))
print("Highest Sale:", max(sales))
print("Lowest Sale:", min(sales))

# Step 3. Statistics
import statistics
print("Mean:", statistics.mean(sales))
print("Median:", statistics.median(sales))
print("Standard Deviation:", statistics.stdev(sales))

# Step 4. Pandas
import pandas as pd
df = pd.DataFrame(sales, columns=["Sales"])
print(df.describe())

# Step 5. Chart
import matplotlib.pyplot as plt
plt.plot(sales, marker="o")
plt.title("Sales Report")
plt.xlabel("Transaction")
plt.ylabel("Sales Amount")
plt.grid(True)
plt.show()
