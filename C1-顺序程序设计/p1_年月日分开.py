# 输入表示年月日的8位数，如“20100722”，输出年、月、日，即“2010年07月22日
ss = '20100722'
year = ss[0:4]
month = ss[4:6]
day = ss[6:8]
print(str(year) + '年'+str(month) +'月' + str(day) + '日')