# q4_测试eval方法的功能
dic1 = {'x':1 , 'y':2}
dic2 = {'z' :3}

res = eval('3*x+ 2*y + z', dic1,dic2)
print(res)