#!/usr/local/python3/bin/python3.6

Goods = [
("iphone",5800),
("ipad",3800),
("mac os",9800)
]

L=[]

for i,value in enumerate(Goods):
    print(i,value)
Momeny = input("请输入你有多少钱:")
if Momeny.isdigit():
    Momeny = int(Momeny)
    #print(type(Momeny))
    while True:
      print("q为退出")
      Num = input("请输入你想要的选项:")
      if Num.isdigit():
         Num = int(Num)
         if Num < len(Goods) and Num >= 0:
            print("购买了",Goods[Num])
            if (Goods[Num][1]) < Momeny:
               Momeny -= Goods[Num][1]
               L.append(Goods[Num][0])
               print("购物车物品：",L)
               print("还剩下 [%s]￥" % Momeny)
            else:
               print("钱不够")
         else:
            print("你输入的选项不存在")
      elif Num == 'q':
         if L:
            exit(print("本次购物品: %s,花了%s元" % (L,Momeny)))
         else:
            exit(print("本次没有购物"))
