# 输入两个点，建立起直线方程y=kx+b。输入第3个点，求点到直线的距离。
# 算法：d=│kx0-y0+b│/√（k²＋1）
import math

x1, y1, k, b = map(float, input().split())
d = abs(k * x1 - y1 + b) / math.sqrt(k ** 2 + 1)

print("点到直线的距离为: ", d)
