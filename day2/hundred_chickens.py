"""
百钱百鸡问题：
公鸡5元/只,母鸡3元/只,小鸡1元3只。如果用100元买100只,三种鸡数目多少？
"""
#x公鸡, y母鸡, z小鸡。公鸡最多20只, 母鸡最多33只。
print("穷举法")
for x in range(0,20):
    for y in range(0,33):
        if 5 * x + 3 * y + 1 / 3 * (100 - x - y) == 100:
            print('公鸡：%s 母鸡：%s 小鸡：%s'%(x , y , 100 - x - y))