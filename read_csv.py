import pandas as pd
d = pd.read_csv("concrete.csv",delimiter=",",names=("no","cement","slag","flyash","water","sp","ca","fa","slump", "flow","cs"))
d= d.iloc[1:]
maxcs = d["cs"].max()
print(d.loc())
print(d.loc[d['cs']== maxcs,])
