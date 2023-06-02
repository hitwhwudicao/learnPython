# 输入平面上第1象限中的1个点的坐标，第3象限中的1个点的坐标，计算两点间的距离
import  math
x1,y1,x2,y2 = map(float , input('请输入平面上第1象限中的1个点的坐标，第3象限中的1个点的坐标:\n').split())

distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 )
print('两点距离为：',distance)

