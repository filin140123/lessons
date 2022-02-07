import pandas as pd

column = ["Mary", "John", "Jane", "David"]
titled_column = {"Name": column, "Height": [1.67, 1.80, 1.78, 1.75], "Weight": [54, 90, 80, 72]}
data = pd.DataFrame(titled_column)

bmi = []
for i in range(len(data)):
    bmi_score = round(data["Weight"][i] / (data["Height"][i] ** 2), 2)
    bmi.append(bmi_score)

data["BMI"] = bmi

data.to_csv("bmi.csv")

print(data)
