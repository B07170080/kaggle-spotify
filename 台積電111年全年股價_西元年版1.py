#台積電111年全年股價
#下載 JSON 轉存成 CSV
import requests
import json
import csv
import os
import time
import pandas as pd
import matplotlib.pyplot as plt

def add_month(i):
        zero="0"
        num=zero+str(i)
        length=len(num)
        num=num[length-2:length]
        return num

def AD(data):
    data[0]=data[0].replace("111","2022")
    data[0]=data[0].split("/")
    data[0]="-".join(data[0])
    return data
    

def writer_csv(filename):
    if not os.path.exists(filename):
        for i in range(1,13):
            url=urlbase+add_month(i)+urltail
            #print(url)
            time.sleep(1)
          
            resp=requests.get(url)
            js=json.loads(resp.text)
            
            
            

            with open(filename,'a',encoding='utf-8-sig',newline="")as fp:
                csv_writer=csv.writer(fp)
                if i==1:    
                    csv_writer.writerow(js['fields'])
                    
                for data in (js['data']):
                    new_data=AD(data)
                    csv_writer.writerow(new_data)
                   

    else:
        print("已有台積電2022全年股價資料")
        
def  plot_chart(d):
    read=pd.read_csv(d)
    read["日期"] = pd.to_datetime(read["日期"])
    print(read['日期'])
    read.plot(kind="line", figsize=(12,6), x="日期", y=["收盤價","最低價","最高價"])
  
    plt.title("2022年一月台積電股票走勢圖", fontsize=20)
    plt.xlabel("日期", fontsize=14)
    plt.ylabel("金額", fontsize=14)
    
     
    
      
            
if __name__ == "__main__":
    urlbase = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2022'
    urltail = '01&stockNo=2330'
    filename = 'stockyear2022.csv'
    
    writer_csv(filename)
    d=filename
    plot_chart(d)
    
    print("完成")