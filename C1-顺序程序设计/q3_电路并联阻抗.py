# q3_电路并联阻抗,使用格式化字符串 %6.2f 6个字符，保留两位小数
# 算法 1/R = 1/r1 + 1/r2
print('请输入两个并联电阻的阻抗：')
r1,r2 = map(float , input().split(' '))
res =  1/(1/r1+1/r2)
print('并联电阻的阻抗为 ：' + '%.2f'%res)
# print('结果的二进制表示为 ', bin(int(res)))
print('87号字符为 ',chr(87))
print('W字符的编码为' ,ord('W'))
