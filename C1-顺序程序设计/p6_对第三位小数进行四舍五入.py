# 输入一个小数，对第三位小数进行四舍五入，保留两位小数

x = float(input('请输入一个三位小数'))
x = x + 0.005
print('三位小数四舍五入之后为：%.2f'%x)