import webbrowser
import pandas as pd
import os as o
import jinja2
import time


df = pd.read_csv('data.csv', encoding='utf-8')
df.columns = ['이름', '링크']
year2020 = df[df['링크'].str.contains('2021')].index
df.drop(year2020, inplace=True)
namechannel = df[df['이름'].str.contains('님의 채널')].index
df.drop(namechannel, inplace=True)
link_name = df['링크']
val_list = link_name.values.tolist()
#print(link_name)


for i in range(3):
    link = val_list[i]
    webbrowser.open(link)
    time.sleep(2)
    print(link)