#导入可能用到的相关库 使用kernel为python3.9 Conda
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

class Y60s: #雅虎金融港股的60天交易数据
    _url = 'https://finance.yahoo.com/quote/{code}.HK/history?p={code}.HK' #构造URL
    
    def get_dt(self, code):
        url = self._url.format(code = code)
        r = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (HTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'}) #发送请求
        r.raise_for_status() #检查网页状态
        soup = BeautifulSoup(r.text, "lxml") #解析网页
        table = soup.find("div",{"id":"Main"}).find("table",{"data-test": "historical-prices"}) #获取60天历史记录
        name = soup.find("h1",{"class":"D(ib) Fz(18px)"}).text #截取股票名称
        dt1 = []
        trs = table.find_all("tr")
        for tr in trs:
            cells = tr.find_all(["th", "td"])
            row = []
            for cell in cells:
                row.append(cell.text.strip(""))
            dt1.append(row)
            df = pd.DataFrame(dt1[1:61], columns = dt1[0]) #第1列到61列为从上至下的历史日期,第0列变成列名
            df = df.set_index(keys="Date") 
        return df,name