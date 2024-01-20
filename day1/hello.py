print('hello world')
"""多行
注释"""

#单行注释
#单行注释

"""
分支结构
if_else 用缩进
"""
print('计算分段函数求值')
print('f(x)=3x - 5 (x > 1)\n')
print('f(x)=x + 2 (-1 <= x <= 1)\n')
print('f(x)=5x + 3 (x > 1)\n')
print('输入x的值: \n')
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x , y))

"""
循环结构
for-in
语法: for x in 
while
语法: while True:
        if
        elif
        else:
            break
"""

