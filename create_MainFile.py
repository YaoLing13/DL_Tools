# coding:utf-8

import os
import random

if __name__ == '__main__':
    path = os.getcwd()
    dataAnnotated = os.listdir(path + '/Annotations')
    dataNum = len(dataAnnotated)  # 数据集数量

    ftest = open('ImageSets/Main/test.txt', 'w')  # 测试集
    ftrain = open('ImageSets/Main/train.txt', 'w')  # 训练集
    ftrainval = open('ImageSets/Main/trainval.txt', 'w')  # 训练验证集
    fval = open('ImageSets/Main/val.txt', 'w')  # 验证集
    testScale = 0.1  # 测试集占总数据集的比例
    valScale = 0.1  # 测试集占总数据集的比例
    trainScale = 0.8  # 训练集占训练验证集的比例

    i = 1
    testNum = int(dataNum * testScale)  # 测试集的数量
    valNum = int(dataNum * testScale)  # 验证集的数量
    trainNum = int((dataNum - testNum) * trainScale)  # 训练集的数量

    test_val_num = []
    for j in range(testNum+valNum):
        test_val_num.append(random.randint(0, dataNum-1))

    testleng = int((testScale/(testScale+valScale))*len(test_val_num))
    test_num = test_val_num[:testleng]
    val_num = test_val_num[testleng:]

    for name in dataAnnotated:
        if i in test_num:
            print>>ftest, name[0:11]
        elif i in val_num:
            print>>fval, name[0:11]
            print>>ftrainval, name[0:11]
        else:
            print>>ftrain, name[0:11]
            print>>ftrainval, name[0:11]
        i += 1
        print(i)
    ftrain.close
    ftrainval.close
    fval.close
    ftest.close
print('done!')
