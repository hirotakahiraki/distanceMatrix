
# coding: utf-8

# In[114]:


import csv
import googlemaps
import pandas as pd
from pandas.io.json import json_normalize

gmaps = googlemaps.Client(key='AIzaSyCJO7jemiz9L5lKaY0k7ZplOD-iFeRhPUc')

file =open("csv/distance.csv",encoding='cp932')

df = pd.read_csv(file)    #csvをdataframe型に変換して読み込み

df['距離']=df['距離'].astype(str)
df['時間']=df['時間'].astype(str)
df['移動手段']=df['移動手段'].astype(str)
default_mode= ["driving", "walking", "bicycling", "transit"]
travel_mode = default_mode[0]#ここで移動モードを選ぶ

for index in df.index.values:
    row = df.iloc[index,[0,1,2,3,4]]
    origins =row[0]
    destinations = row[1]
    df.at[index,'移動手段']=travel_mode
    
    matrix = gmaps.distance_matrix(origins, destinations, mode=travel_mode)

    df.at[index,"距離"] = matrix["rows"][0]["elements"][0]["distance"]["text"]
    df.at[index,"時間"] = matrix["rows"][0]["elements"][0]["duration"]["text"]
    

df.to_csv("csv/distance_output.csv", encoding="shift_jis")


# In[111]:


file =open("csv/distance_output.csv",encoding='cp932')

df = pd.read_csv(file)
print(df)

