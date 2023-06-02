# q2_解三角形，给出三角形两边及夹角求第三边
# 余弦定理 cosm = (a**2+b**2-c**2) /2ab ，m 为其夹角(单位为度)
import  math
x = input('请输入三角形两边及夹角（夹角应当小于180度）以空格分割：').split(' ')
a,b,m = x
res = math.sqrt(float(a)**2 + float(b)**2 - 2*float(a)*float(b)*math.cos(math.pi*float(m)/180))
print('第三边的长度为 '+ str(res))
