import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import requests as rq

r = rq.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vSggXriX8oabs8CBQP9Gf1CiWlgt5bJPWN3pUkS5VCwN0bubrQiXpVm9h8qLVGQv4BxJTSW8C8x1hXL/pub?gid=0&single=true&output=csv')
#https://docs.google.com/spreadsheets/d/e/2PACX-1vSggXriX8oabs8CBQP9Gf1CiWlgt5bJPWN3pUkS5VCwN0bubrQiXpVm9h8qLVGQv4BxJTSW8C8x1hXL/pub?gid=0&single=true&output=csv
#https://raw.githubusercontent.com/pranjalm/iter_dir/master/section_c.csv
data = r.content
df = pd.read_csv(BytesIO(data), index_col=0, header=None)
df = df.T

df.rename(columns={'Discharge of strip (m3/s)':'discharge',
                         'Total water depth (m)':'depth',
                         'Distance across stream (m)':'distance'},
                inplace=True)

fig = plt.figure()
plt.plot(df['distance'],df['depth'])
plt.gca().invert_yaxis()
plt.xlabel('Distance across stream (m)', fontsize=18)
plt.ylabel('Depth (m)', fontsize=16)
fig.savefig('test.jpg')


# a = input().strip().split("/")
# print(a)
print(type(df))
print(df.head())
