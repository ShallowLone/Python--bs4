import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Data.csv") #读取csv文件

#试错
try: #转换数据类型
    df["Date"]=pd.to_datetime(df["Date"])
    df[["Open", "High", "Low", "Close*", "Adj Close**"]]=df[["Open","High","Low","Close*","Adj Close**"]].astype("float")
    df["Volume"]=df["Volume"].apply(lambda x: x.replace(",","")).astype("int")
except:
    print("Error")
    raise()
else:
    pass


df=df.set_index("Date",drop=True)
df["ma5"]=df["Adj Close**"].rolling(5).mean() #五天移动平均值
df["ma10"]=df["Adj Close**"].rolling(10).mean() #十天移动平均值
df["ma15"]=df["Adj Close**"].rolling(15).mean() #十五天移动平均值
df["pos"]=df[["ma5","ma10"]].apply(lambda x:int(x["ma5"]>=x["ma10"]),axis=1)
pic=df[["Adj Close**","ma5","ma10","ma15"]].plot(title="Some price and moving average of the stock")
fig=pic.get_figure()
fig.savefig("数据.png")
print(df)