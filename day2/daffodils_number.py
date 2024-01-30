
"""
find all daffodils numbers
水仙花数:3位数,每位数的立方之和等于数本身

( // 整除操作符---返回除法运算的商的整数部分 )
"""

for num in range(100 , 1000):
    low = num % 10
    mid = num // 10 %10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

    """
    num = 245
    low = 5
    mid = (245/10)%10 = 4
    high = (245/100)%10 = 2
    
    """
