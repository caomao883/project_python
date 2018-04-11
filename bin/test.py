


import numpy as np
import pandas as pd

df = pd.read_excel("../data/t1.xlsx",sheetname="数据段1")
names = df.columns.values
print(names)
print(names[7])
print(names[10])
data = np.array(df)


for i,item in enumerate(data):
    arr1 = item[7]
    arr2 = item[10]
    if arr1.__contains__("烟油"):
        print(arr1)
        print(arr2)
        if arr1.endswith("mg") and not arr2.endswith("mg"):
            arr = arr1.split(" ")
            item[10] = arr2 + arr[-1]


result_df = pd.DataFrame(data,columns=names,index=None)
result_df.to_excel("result.xlsx")


