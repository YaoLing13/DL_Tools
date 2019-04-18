# pr_curve.py
# coding:utf-8
 
import numpy as np
import matplotlib.pyplot as plt
 
data=np.loadtxt('PR.txt')
mean=np.mean(data[:,1:],axis=1)
tick=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
#
# plt.figure()
# plt.subplot(2,2,1)
# plt.title('Cyclist, AP=0.722')
# plt.xlabel('Recall')
# plt.ylabel('Precision')
# plt.axis([0, 1, 0, 1.05])
# plt.xticks(tick)
# plt.yticks(tick)
# plt.plot(data[:,0],data[:,1])
 
# plt.subplot(2,2,2)
plt.figure()
# plt.figure(1)
plt.title('Car, AP=0.764168')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.axis([0, 1, 0, 1.05])
plt.xticks(tick)
plt.yticks(tick)
lns1=plt.plot(data[:,0],data[:,1],'b',label = "Car")
# plt.savefig('car-pr.png')
 
# plt.subplot(2,2,3)
# plt.figure(2)
plt.title('Person, AP=0.773486')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.axis([0, 1, 0, 1.05])
plt.xticks(tick)
plt.yticks(tick)
lns2=plt.plot(data[:,0],data[:,2],'g',label = "Person")
# plt.savefig('person-pr.png')

# plt.subplot(2,2,4)
# plt.figure(3)
#plt.title('P-R Curve')
plt.title('Overall, mAP=0.768827')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.axis([0, 1, 0, 1.05])
plt.xticks(tick)
plt.yticks(tick)
lns3=plt.plot(data[:,0],mean,'r',label="Overall")

lns = lns1 + lns2 + lns3
labs = [l.get_label() for l in lns]
plt.legend(lns, labs, loc=0)

plt.savefig('all.png')
plt.show()

