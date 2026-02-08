import pandas as pd

data = {
    "Id": [1, 2, 3, 4],
    "Name": ["Pankaj", "Meghna", "David", "Lisa"],
    "Role": ["CEO", None, None, None],
    "Salary": [100, 200, None, None]
}

df = pd.DataFrame(data)
print(df)
