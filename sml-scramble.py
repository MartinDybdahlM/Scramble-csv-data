import pandas as pd
import numpy as np


## Path to file (No header in csv)
df = pd.read_csv("data.csv", header=None) 
df = df.to_numpy()

names = []
new_names = []

# New base-names for entries in each column
label = ["Prod","RawMat","MouldTyp", "BoxCont", "BoxLayout", "MachType", "Vend"]
j = 0

# Specify which columns to update (0-indexed)
col = [1,4,11,17,18,19,25]



for e in range(len(col)):
    col_value = col[e]
    data = df[:,col_value]
    for i in range(len(data)):
        if (data[i] in names) == False:
            names.append(data[i])
            data[i] = label[e] + "-" + str(j)
            new_names.append(data[i])
            j+=1
        else:
            index = names.index(data[i])
            data[i] = new_names[index]
    j = 0
    names = []
    new_names = []
    for l in range(len(df[col_value])):
        df[l, col_value] = data[l]


pd.DataFrame(df).to_csv("n_data.csv")

print("DONE!")

