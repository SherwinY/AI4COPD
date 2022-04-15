import pandas as pd
import xlwt
import openpyxl

df1 = pd.read_excel('excel1.xlsx')
df2 = pd.read_excel('excel2.xlsx')

book = openpyxl.load_workbook('excel3.xlsx')
sheet = book.active

#将excel2中氧分压检验结果和excel1中检查结果整合到一个excel表中
h = 2
l = 196
for i in df1['登记号'].tolist():
    df3 = df2.loc[(df2['登记号'] == i), ['登记号', '化验结果项目名称', '定量结果']]
    djh = df3.iloc[:]['登记号']
    djhlist = djh.tolist()
    name = df3.iloc[:]['化验结果项目名称']
    namelist = name.tolist()
    data = df3.iloc[:]['定量结果']
    datalist = data.tolist()
    for num in range(len(namelist)):
        if namelist[num] == '氧分压':
            sheet.cell(row=h, column=l, value=datalist[num])
            break
    h = h + 1

book.save('result.xlsx')