# coding:utf-8
import numpy as np
import pandas as pd


df = pd.read_excel("data/t.xlsx",header=None)
data = np.array(df)
data = list(data)
new_data = []
se = set()
for line in data:

    if not se.__contains__(str(line[0])+str(line[1])):
        se.add(str(line[0])+str(line[1]))
        new_data.append(list(line))
print(new_data)
df = pd.DataFrame(new_data,index=None,columns=None)
df.to_excel("data/t2.xlsx",index=None,columns=None,header=None)
