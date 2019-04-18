# pr_curve.py
# coding:utf-8

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# mpl.rcParams[u'font.sans-serif'] = ['simhei']
# mpl.rcParams['axes.unicode_minus'] = False



f = open("mapfps.txt","r")
lines = f.readlines()      #读取全部内容 ，并以列表方式返回
fig = plt.figure()
ax = plt.subplot(111)
datas=[]
for line in lines:
    data = line.split()
    datas.append(data)

tx = [0.5,0.55,0.60,0.65,0.70,0.75,0.80]
# ty = [0,10,20,30,40,50,60,70,80,90]
# plt.xticks(ty)
plt.ylim((0.55,0.8))
plt.xlim((0,90))
#plt.title('Accuracy VS Speed')
plt.xlabel('Speed (FPS on GTX1060)')
plt.ylabel('Accuracy (mAP)')
area = [80]
l1 = ax.scatter(float(datas[0][2]), float(datas[0][1]), s=area, color='g', marker='^', label="SSD300")
l2 = ax.scatter(float(datas[1][2]), float(datas[1][1]), s=area, color='g', marker='o', label="DSSD321")
l3 = ax.scatter(float(datas[2][2]), float(datas[2][1]), s=area, color='m', marker='<', label="R-SSD300")
l4 = ax.scatter(float(datas[3][2]), float(datas[3][1]), s=area, color='m', marker='h', label="YOLOv2")
l5 = ax.scatter(float(datas[4][2]), float(datas[4][1]), s=area, color='b', marker='p', label="Tiny-YOLOv2")
l6 = ax.scatter(float(datas[5][2]), float(datas[5][1]), s=area, color='b', marker='v', label="SSD-MobileNet")
l7 = ax.scatter(float(datas[6][2]), float(datas[6][1]), s=area, color='r', marker='s', label="DupNet(proposed)")
l8 = ax.scatter(float(datas[7][2]), float(datas[7][1]), s=area, color='r', marker='D', label="DupNet-TensorRT")

# lns = l1+l2+l3+l4+l5+l6+l7+l8
# labs = [l.get_label() for l in lns]
# ax.legend(lns, labs, loc=0)
plt.legend(loc = 'lower right')
plt.savefig('mapfps11.png',dpi=200)
plt.show()
