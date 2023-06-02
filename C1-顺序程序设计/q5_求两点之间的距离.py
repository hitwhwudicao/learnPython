# q5_求两点之间的距离
import  math
x1,y1,x2,y2 = map(float , input().split(' '))
print('({},{})'.format(x1,y1) + ' 与({},{}) '.format(x2,y2)+'之间的距离为：%.2f'%math.sqrt( (x1-x2)**2 + (y1-y2)**2) )