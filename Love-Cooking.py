import tkinter
from tkinter import*
import tkinter.font as tkFont
import requests
import bs4
import base64
from base64 import urlsafe_b64decode
import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen
from PIL import Image, ImageTk
import requests
import random
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import os

def third(ingredients,number):
    
    #matplotlib.use('TkAgg')
    n=0
    labels=[]   # 圓餅圖需要的資料
    sizes=[]
    
    for ingredient in ingredients:
        
        labels+=[ingredient.text] # 圓餅圖需要的資料
        sizes+=[1] # 圓餅圖需要的比例
        n=n+1
        
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] # 中文字體:微軟正黑體
    if n==3:
        #pie.explode=(0,0,0.1)
        plt.pie(sizes,explode=(0,0,0.1),labels=labels,autopct="%1.1f%%",startangle=90,textprops={"fontsize":15})
        plt.axis("equal")
        Canvas_statis.draw()
    if n==4:
        #pie.explode=(0,0,0,0.1)
        plt.pie(sizes,explode=(0,0,0,0.1),labels=labels,autopct="%1.1f%%",startangle=90)
        plt.axis("equal")
        Canvas_statis.draw()
    if n==5:
        #pie.explode=(0,0,0,0,0.1)
        plt.pie(sizes,explode=(0,0,0,0,0.1),labels=labels,autopct="%1.1f%%",startangle=90,textprops={"fontsize":15})
        plt.axis("equal")
        Canvas_statis.draw()
    if n==6:
        #pie.explode=(0,0,0,0,0.1)
        plt.pie(sizes,explode=(0,0,0,0,0.1),labels=labels,autopct="%1.1f%%",startangle=90)
        plt.axis("equal")
        Canvas_statis.draw()
    Canvas_statis.get_tk_widget().place(x=30,y=80)
    if number==1:
        str="""份量 : 4\n\nstep 1 :\n先南瓜外皮清洗乾淨，接著切塊去籽後，放進電鍋蒸至軟透(筷子可以穿過即可)\nstep 2 :\n蒸熟軟透的南瓜連同外皮一起下果汁機打成泥\nstep 3 :\n將南瓜泥加入些許鹽以及約170cc的鮮奶油後，小火起跑泡後即可關火。\nstep 4 :\n盛碗後點入鮮奶油拉花即完成囉
        """
    elif number==2:
        str="""份量 : 4\n\nstep 1 :\n鮭魚蒸熟後用叉子撥散，放入瓷碗中備用；雞蛋打散備用。\nstep 2 :\n水加入調味料，試試味道，比蒸蛋稍微鹹一點點即可。\nstep 3 :\n將調味好的水倒入蛋液中拌勻，過篩倒入裝有鮭魚的瓷碗中。\nstep 4 :\n將蛋液表面氣的泡戳破，再蓋上一層鋁箔紙。\nstep 5 :\n電鍋外鍋先放半杯水，按下煮飯預熱，電鍋跳起後再將瓷碗放入電鍋，外鍋再放半杯水，按下煮飯後計時15分鐘。（如果沒有放鮭魚的話只要10分鐘即可）時間到後即將蒸蛋取出就可以囉。
        """
       
    text.insert(END,str)
    text.place(x=380,y=80)
    
    window.mainloop()
def serving(ingredients,number):
    global urls
    if number==1:
        urls = 'https://icook.tw/recipes/406330'# 爬取網址:南瓜濃湯
    elif number==2:
        urls = 'https://icook.tw/recipes/414453' # 爬取網址:鮭魚蒸蛋
 
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
    }
    htmlFile = requests.get(urls,headers=headers) # 發出網頁需求
    
    objSoup = bs4.BeautifulSoup(htmlFile.text,'html.parser') # 解析網頁
   
    serving = objSoup.find('span',class_='num')#份量
    #print(serving)
    third(ingredients,number)
    
def ingredien(number):
   
    global urls
    global serving
    global step
    #食材、份量、圓餅圖
    if number==1:
        urls = 'https://icook.tw/recipes/406330'# 爬取網址:南瓜濃湯
    elif number==2:
        urls = 'https://icook.tw/recipes/414453' # 爬取網址:鮭魚蒸蛋
 
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
    }
    htmlFile = requests.get(urls,headers=headers) # 發出網頁需求
    
    objSoup = bs4.BeautifulSoup(htmlFile.text,'html.parser') # 解析網頁
   
    #serving = objSoup.find('span',class_='num')#份量
    ingredients = objSoup.find_all('div',class_='ingredient') # 食材
    
    #ingredients
    # 爬蟲抓步驟
   
    #step = objSoup.find_all('p',class_="recipe-step-description-content")
    btn1.place_forget()
    btn2.place_forget()
    btn3.place_forget()
    btn4.place_forget()
    serving(ingredients,number)
    #window.mainloop()
def second(number):
    
    #fontsetting=tkFont.Font(family="Arial",size="16",weight="bold")
    e1.place_forget()
    img1 = Image.open('C:/Users/User/Desktop/期末/images/1.gif')
    img2 = Image.open('C:/Users/User/Desktop/期末/images/2.gif')
    img3 = Image.open('C:/Users/User/Desktop/期末/images/3.gif')
    img4 = Image.open('C:/Users/User/Desktop/期末/images/4.gif')
    img1 = img1.resize((230, 170))
    img2 = img2.resize((230, 170))
    img3 = img3.resize((230, 170))
    img4 = img4.resize((230, 170))
    p1 = ImageTk.PhotoImage(img1)
    p2 = ImageTk.PhotoImage(img2)
    p3 = ImageTk.PhotoImage(img3)
    p4 = ImageTk.PhotoImage(img4)
    if number==1:
        label1.config(text=foodname[0])
        btn3.config(text='',image=p3,relief=FLAT)
        btn4.config(text='',image=p4,relief=FLAT,command=lambda:ingredien(1))
    
    elif number==2:
        label1.config(text=foodname[1])
        btn3.config(text='',image=p4,relief=FLAT,command=lambda:ingredien(2))
        btn4.config(text='',image=p3,relief=FLAT)
        
    btn1.config(text='',image=p1,relief=FLAT)
    btn2.config(text='',image=p2,relief=FLAT)
    
    label1.place(x=180,y=10)
    btn1.place(x=70,y=80)
    btn2.place(x=370,y=80)
    btn3.place(x=70,y=290)
    btn4.place(x=370,y=290)
    window.mainloop()
   
    
def foodimage(number):
   
    #global htmlfile
    
    image_links2=[]
    
    if number==1:
        url='https://icook.tw/search/%E5%8D%97%E7%93%9C%E6%BF%83%E6%B9%AF/'
    elif number==2:
        url=' https://icook.tw/search/%E8%92%B8%E8%9B%8B/'
    
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
      }
    htmlfile=requests.get(url,headers=headers)
    
    htmlfile.encoding='utf-8' 
    sp=bs4.BeautifulSoup(htmlfile.text,'html.parser')
    results=sp.find_all('img',class_='browse-recipe-cover-img lazyload', limit=4)
    
    
    image_links1 = [result.get("data-src") for result in results]  # 取得圖片來源連結
    
    
    for index, link in enumerate(image_links1):
 
        if not os.path.exists("images"):
            os.mkdir("images")  # 建立資料夾
 
        img = requests.get(link)  # 下載圖片
        #print(img)
        with open("images\\" + str(index+1) + ".gif", "wb") as file:  # 開啟資料夾及命名圖片檔
            file.write(img.content) 
        file.close()
    e1.place_forget()
    second(number)
    
    
    
def first_section():
    
    
  
    btn1.config(text=foodname[0],command=lambda:foodimage(1))
    btn2.config(text=foodname[1],command=lambda:foodimage(2))
    btn3.config(text=foodname[2])
    btn1.place(x=110,y=80)
    btn2.place(x=110,y=135)
    btn3.place(x=110,y=190)
   
    
def food_name():
    global foodname
    #global htmlfile
    global url
    if e1.get()=='南瓜':
        url='https://icook.tw/search/%E5%8D%97%E7%93%9C/'
    elif e1.get()=='蛋':
        url='https://icook.tw/search/%E8%9B%8B/'
    headers = {
      'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
      }
    htmlfile=requests.get(url,headers=headers)
    #print(htmlfile)
    htmlfile.encoding='utf-8' 
    soup=bs4.BeautifulSoup(htmlfile.text,'lxml')
    foods=soup.find_all('a',class_='filters-recipe-link')
   # print(foods)
    for food in foods:
        fo_name=food.get('data-keyword')
        #dict1={"編號":n,"公司名稱":co_name,"職務名稱":job_name}
        #print(fo_name)
        foodname.append(fo_name)
    first_section()




url='https://icook.tw/search/%E5%8D%97%E7%93%9C/'
"""
#url='https:%2F%2Ficook.tw%2Fsearch%2F%25E5%258D%2597%25E7%2593%259C%2F'
headers = {
      'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
      }
htmlfile=requests.get(url,headers=headers)
    #print(htmlfile)
htmlfile.encoding='utf-8' 
"""
foodname=[] 

window=Toplevel() 
#window=Tk()

window.title("愛料理")
window.geometry("700x500")
window.config(bg="white")

img_res = Image.open('researsh1.gif')
img1_res = img_res.resize((50, 50))
p1_res = ImageTk.PhotoImage(img1_res)



fontsetting=tkFont.Font(family="Arial",size="16",weight="bold")
fontsetting_1=tkFont.Font(family="Arial",size="11")
label1=Label(window,text='輸入食材 :',bg="white",width=24,height=2,font=fontsetting)
text=Text(window,height=30,width=30,font=fontsetting_1,relief=FLAT)
e1=Entry(window,bg='white',bd=3,width=15,font=fontsetting,relief=GROOVE)
btn1=tkinter.Button(window,bg="white",relief=GROOVE,font=fontsetting)
btn2=tkinter.Button(window,bg="white",relief=GROOVE,font=fontsetting)
btn3=tkinter.Button(window,bg="white",relief=GROOVE,font=fontsetting)
btn4=tkinter.Button(window,image=p1_res,relief=FLAT,bg="white",command=food_name)

pie=plt.figure(figsize=(4.2,4.2))
Canvas_statis=FigureCanvasTkAgg(pie,window)


label1.place(x=5,y=15)
e1.place(x=230,y=28)
btn4.place(x=450,y=20)

window.mainloop()




def wirte_csv():
    #print(foodname)
    f_name='foodname.csv'
    with open(f_name,'w',newline="",encoding='utf-8-sig')as csvfile:
        #fields=["編號","公司名稱","職務名稱"]
        Writer=csv.writer(csvfile,delimiter="\t")
        
        #dictWrite.writeheader()
        for row in foodname:
            Writer.writerow(row)



 

