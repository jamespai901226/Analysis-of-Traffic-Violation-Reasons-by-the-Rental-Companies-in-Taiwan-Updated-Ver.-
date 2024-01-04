from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import cv2
import ddddocr
import time
import csv
import jieba
import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt   # 資料視覺化套件
from selenium.webdriver.chrome.options import Options
import math
#輸入快捷
d = { "1" : { "Name" : "格上租車", "abb" : "格上", "IDinput" : "12208883"},
      "2" : { "Name" : "和運租車", "abb" : "和運", "IDinput" : "70364778"},
      "3" : { "Name" : "Zipcar", "abb" : "Zipcar", "IDinput" : "53799460"} }
while True:
    name = input("請輸入1或2或3選擇查詢租車公司：1.格上租車 2.和運租車 3.Zipcar\n")
    if name in d:
        print("您輸入的是:", d[name]["Name"])
        print("統一編號是:", d[name]["IDinput"])
        break
    else:
        print("輸入錯誤，請重新輸入")
        continue
print("如程式意外關閉或錯誤，為驗證碼辨識錯誤，請重啟程式")
IDinput = d[name]["IDinput"]
NAMEinput = d[name]["abb"]


#PATH = "C:/Users/Mishima Yuna/Desktop/python/chromedriver_win32/chromedriver.exe"
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get("https://www.mvdis.gov.tw/m3-emv-vil/vil/penaltyQueryPay") #設定網址
action = ActionChains(driver)
legal = driver.find_element("xpath", '//*[@id="legal"]') #按法人按鈕
action.click(legal)
action.perform()
time.sleep(1)

ID2 = driver.find_element("id", 'id2') #抓取統編輸入格
#ID2.clear() #清空預設文字
ID2.send_keys(IDinput)
#ID2.send_keys("12208883") #格上統編
path = "C:/Users/Mishima Yuna/Desktop/python/"
driver.save_screenshot('ss.png')
img = cv2.imread("ss.png")
x = 822 # 裁切區域的 x 與 y 座標（左上角）
y = 659
w = 125 # 裁切區域的長度與寬度
h = 50
crop_img = img[y:y+h, x:x+w] # 裁切圖片
#cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
cv2.imwrite('s.png', crop_img)
ocr = ddddocr.DdddOcr()
with open('s.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)
print(res)
#time.sleep(5)
e = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[1]/div[3]/div/div[2]/form/table/tbody/tr[4]/td/input')
e.clear()  # 清空默认文本
e.send_keys(res)
driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[1]/div[3]/div/div[2]/form/table/tbody/tr[4]/td/input').click()
#time.sleep(3)
enter = driver.find_element("xpath", '//*[@id="search2"]/img')
action.click(enter)
action.perform()
#print("Recaptcha Success")
# 檔案路徑
file = "./ss.png"
file2 = "./s.png"
os.remove(file)
os.remove(file2)
time.sleep(1)
#ID.send_keys(Keys.RETURN) #按ENTER(這裡註解因網站不支援)
#WebDriverWait(driver, 50).until(
#    EC.presence_of_element_Located((By.CLASS_NAME, "caption_std"))) #確認12208883 ，違規紀錄如下：這句話出來再開始抓取，最多等30秒
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);") #向下滾動到網站底部
#辨識頁數
driver.save_screenshot('nn.png')
img = cv2.imread("nn.png")
x = 730 # 裁切區域的 x 與 y 座標（左上角）
y = 465
w = 40 # 裁切區域的長度與寬度
h = 20
crop_img = img[y:y+h, x:x+w] # 裁切圖片
#cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
cv2.imwrite('n.png', crop_img)
ocr = ddddocr.DdddOcr()
with open('n.png', 'rb') as f:
    img_bytes = f.read()
rn = ocr.classification(img_bytes)
file = "./nn.png"
file2 = "./n.png"
os.remove(file)
os.remove(file2)
nrn = "".join(filter(str.isdigit, rn)) #將字串中非數字字元移除
pages = int(nrn)-2
#print(rn)
#print(nrn)
#print(pages)

c = 100/pages
count = 0

pathtxt = 'result.csv'
f = open(pathtxt, 'w', encoding='utf-8')
f.write("公司" + "," + "原因" + "\n")
a = 0
while a <= pages:
    print("第", a,"頁，共", pages, "頁，已完成",math.floor(count*100)/100.0 ,"%")
    date = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[1]/td[2]')  # 擷取文字從1-10
    reason = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[1]/td[3]')
    #print(date.text + "  " + reason.text)
    f.write( NAMEinput + "," + reason.text + "\n")
    date2 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[2]/td[2]')
    reason2 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[2]/td[3]')
    #print(date2.text + "  " + reason2.text)
    f.write( NAMEinput + "," + reason2.text + "\n")
    date3 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[3]/td[2]')
    reason3 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[3]/td[3]')
    #print(date3.text + "  " + reason3.text)
    f.write( NAMEinput + "," + reason3.text + "\n")
    date4 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[4]/td[2]')
    reason4 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[4]/td[3]')
    #print(date4.text + "  " + reason4.text)
    f.write( NAMEinput + "," + reason4.text + "\n")
    date5 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[5]/td[2]')
    reason5 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[5]/td[3]')
    #print(date5.text + "  " + reason5.text)
    f.write( NAMEinput + "," + reason5.text + "\n")
    date6 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[6]/td[2]')
    reason6 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[6]/td[3]')
    #print(date6.text + "  " + reason6.text)
    f.write( NAMEinput + "," + reason6.text + "\n")
    date7 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[7]/td[2]')
    reason7 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[7]/td[3]')
    #print(date7.text + "  " + reason7.text)
    f.write( NAMEinput + "," + reason7.text + "\n")
    date8 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[8]/td[2]')
    reason8 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[8]/td[3]')
    #print(date8.text + "  " + reason8.text)
    f.write( NAMEinput + "," + reason8.text + "\n")
    date9 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[9]/td[2]')
    reason9 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[9]/td[3]')
    #print(date9.text + "  " + reason9.text)
    f.write( NAMEinput + "," + reason9.text + "\n")
    date10 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[10]/td[2]')
    reason10 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[10]/td[3]')
    #print(date10.text + "  " + reason10.text)
    f.write( NAMEinput + "," + reason10.text + "\n")
    enter = driver.find_element("xpath", '//*[@id="next"]/img')
    action.click(enter)
    action.perform()
    #print(a)
    a = a + 1
    count = count + c
    time.sleep(1)
else:
    #print("Web closed")
    time.sleep(5)
    driver.quit()
f.close

path2 = 'NAMEinput.txt'
f = open(path2, 'w', encoding="utf-8")
print(NAMEinput, file=f)
f.close();
start_dire = r"./chart.py"
os.system("python %s" %start_dire)

