# pr_curve.py
# coding:utf-8

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams[u'font.sans-serif'] = ['simhei']
mpl.rcParams['axes.unicode_minus'] = False

traindata=np.loadtxt('VOC-train.log')   ## 4 cols: iter,  second,  loss,      learningrate
testdata=np.loadtxt('VOC-test.log')     ## 3 cols: iter,  second,  testAccu

trainx = [0,5000,10000,15000,20000,25000,30000,35000,40000,45000]
trainy = [0,1,2,3,4,5,6]
testy = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
# plt.title('Train loss')
# plt.xlabel('Iter')
# plt.ylabel('Loss')
# plt.axis([0, 1, 0, 1.05])
# plt.xlabel('Iter')

# plt.xticks(trainx)
# plt.yticks(trainy)
# plt.plot(traindata[:,0],traindata[:,2])
# plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(111)
lns1 = ax1.plot(traindata[:,0],traindata[:,2],'r',label=u"训练集损失曲线")
ax2 = ax1.twinx() # this is the important function
lns2 = ax2.plot(testdata[:,0],testdata[:,2], 'g',label = u"验证集精确度曲线")

lns = lns1 + lns2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=0)

# ax1.legend(loc=1)
ax1.set_ylabel(u'损失值')
# ax2.legend(loc=2)
ax2.set_ylabel(u'精确度')
ax2.set_ylim(0, 1)

ax1.set_xlabel(u'迭代次数')
plt.savefig('trainlog.png')
plt.show()