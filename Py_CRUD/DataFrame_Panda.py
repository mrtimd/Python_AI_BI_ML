#DataFrame_Panda.py
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

print("#Load dataframe from a variable")
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df.loc["day2"])

print("#Load a comma separated file (CSV file) into a DataFrame:")
csvdf = pd.read_csv('data.csv')
print(csvdf) 