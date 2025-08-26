# 📝 Sales Analysis Starter Script

# Step 1. Load the Data
with open("sales.txt", "r") as file:
    sales = [____(line.strip()) for line in file]

print(sales)

# Step 2. Basic Math
print("Total Sales:", ____(sales))
print("Average Sale:", sum(sales) / ____(sales))
print("Highest Sale:", ____(sales))
print("Lowest Sale:", ____(sales))

# Step 3. Statistics
import statistics
print("Mean:", statistics.____(sales))
print("Median:", statistics.____(sales))
print("Standard Deviation:", statistics.____(sales))

# Step 4. Pandas
import pandas as pd
df = pd.DataFrame(sales, columns=["Sales"])
print(df.____())

# Step 5. Chart
import matplotlib.pyplot as plt
plt.plot(sales, marker="o")
plt.title("Sales Report")
plt.xlabel("Transaction")
plt.ylabel("Sales Amount")
plt.show()
