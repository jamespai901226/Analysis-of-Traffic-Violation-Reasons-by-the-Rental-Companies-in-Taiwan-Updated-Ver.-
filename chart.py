import os
import time
import csv
import jieba
import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt   # 資料視覺化套件

import math
# 設定CSV檔路徑和關鍵字
csv_file = './result.csv'

path2 = 'NAMEinput.txt'
f = open(path2, 'r', encoding='utf-8')
#print(f.read())
NAMEinput = f.read()
f.close()
os.remove(path2)

# 設定CSV檔路徑和關鍵字
csv_file = './result.csv'
keyword = NAMEinput
def search_keyword(csv_file, keyword):
    count = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword in seg_list:
                    count += 1
    return count



# 呼叫函式並輸出結果
result = search_keyword(csv_file, keyword)
keyword2= '停車'
def search_keyword2(csv_file, keyword2):
    count2 = 0

    with open(csv_file, 'r', encoding='utf-8') as file2:
        reader = csv.reader(file2)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword2 in seg_list:
                    count2 += 1

    return count2

result2 = search_keyword2(csv_file, keyword2)
print(f'中文關鍵字 "{keyword2}" 在CSV檔中出現了 {result2} 次。')


keyword3= '20'
def search_keyword3(csv_file, keyword3):
    count3 = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword3 in seg_list:
                    count3 += 1

    return count3

result3 = search_keyword3(csv_file, keyword3)
print(f'中文關鍵字 "{keyword3}" 在CSV檔中出現了 {result3} 次。')

keyword4= '40'
def search_keyword4(csv_file, keyword4):
    count4 = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword4 in seg_list:
                    count4 += 1

    return count4

result4 = search_keyword4(csv_file, keyword4)
print(f'中文關鍵字 "{keyword4}" 在CSV檔中出現了 {result4} 次。')

keyword5= '60'
def search_keyword5(csv_file, keyword5):
    count5 = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword5 in seg_list:
                    count5 += 1

    return count5

result5 = search_keyword5(csv_file, keyword5)
print(f'中文關鍵字 "{keyword5}" 在CSV檔中出現了 {result5} 次。')

keyword6= '燈光'
def search_keyword6(csv_file, keyword6):
    count6 = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword6 in seg_list:
                    count6 += 1
    return count6

result6 = search_keyword6(csv_file, keyword6)
print(f'中文關鍵字 "{keyword6}" 在CSV檔中出現了 {result6} 次。')

keyword7= '標線'
def search_keyword7(csv_file, keyword7):
    count7 = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword7 in seg_list:
                    count7 += 1

    return count7

result7 = search_keyword7(csv_file, keyword7)
print(f'中文關鍵字 "{keyword7}" 在CSV檔中出現了 {result7} 次。')

keyword8= '方向'
def search_keyword8(csv_file, keyword8):
    count8 = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword8 in seg_list:
                    count8 += 1

    return count8

result8 = search_keyword8(csv_file, keyword8)
print(f'中文關鍵字 "{keyword8}" 在CSV檔中出現了 {result8} 次。')
'''
result9 = result - result2 - result3 - result4 - result5 - result6 - result7 - result8

print(str(result9))
'''



def search_key(csv_file, key):
    c = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if key in seg_list:
                    c += 1

    return c


#print(str(result9))
pathtxt = 'result-EN.csv'
f = open(pathtxt, 'w')
f.write("Reason" + "," + "Count" + "\n")
f.write("Illegal Parking" + "," + str(result2) + "\n")
f.write("Speeding Under 20" + "," + str(result3)  + "\n")
f.write("Speeding Under 40" + "," + str(result4) + "\n")
f.write("Speeding Under 60" + "," + str(result5) + "\n")
f.write("Running a Red Light" + "," + str(result6) + "\n")
f.write("Not Following Marks" + "," + str(result7) +  "\n")
f.write("Not Using Turn Signal" + "," + str(result8) + "\n")
f.write("Other" + "," + str(result2) + "\n")

f.close()

accident = pd.read_csv("./result-EN.csv")

plt.figure(figsize=(13, 13))  # 顯示圖框架大小

labels = accident["Reason"]  # 製作圓餅圖的類別標籤
separeted = (0, 0, 0.3, 0, 0.3)  # 依據類別數量，分別設定要突出的區塊
size = accident["Count"]  # 製作圓餅圖的數值來源
total = 2087
def make_autopct(size):
    def my_autopct(pct):
        total = sum(size)
        val = int(round(pct*total/100.0))
        # 同时显示数值和占比的饼图
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
plt.pie(size,  # 數值
        labels = labels,  # 標籤
        autopct = make_autopct(size),
        pctdistance = 0.6,  # 數字距圓心的距離,
        textprops = {"fontsize": 12},  # 文字大小
        shadow = True )  # 設定陰影
plt.axis('equal')  # 使圓餅圖比例相等
plt.title("Pie Chart of Violate Traffic Law", {"fontsize": 18})  # 設定標題及其文字大小
plt.legend(loc="best")  # 設定圖例及其位置為最佳
plt.savefig("./Pie chart of violate traffic law.png",  # 儲存圖檔
            bbox_inches='tight',  # 去除座標軸占用的空間
            pad_inches=0.0)  # 去除所有白邊

plt.figure(figsize=(16, 10))  # 顯示圖框架大小


x = labels
h = size
plt.bar(x,h)
plt.title("Bar Chart of Violate Traffic Law", {"fontsize": 18})# 設定標題及其文字大小
plt.savefig("./Bar chart of violate traffic law.png")
print("CSV及統計圖檔案已儲存")

plt.show()
plt.close()  # 關閉圖表
