from math import log
import operator as op

dataset = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
def createDataSet():
    dataset = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no sufacing', 'flippers']
    return dataset, labels

def calEnt():
    """计算某列（特征）的信息熵"""
    #创建分类计数字典
    numEntries = len(dataset)
    labelcount = {}
    for feat in dataset:
        currentlabel = feat[-1]
        if currentlabel not in labelcount:
            labelcount[currentlabel] = 0
        labelcount[currentlabel] += 1

    #计算熵
    ent = 0.0
    for key in labelcount:
        pro = float(labelcount[key])/numEntries
        ent += -1*pro*log(pro,2)
    return



#通过排序返回出现次数最多的类别
#参数clsslist是响应变量集
def majorityCnt(classlist):
    classcount={}
    for vote in classlist:
        if vote not in classcount.keys():
            classcount[vote] = 0
        classcount[vote] += 1
    sortedclasscount = sorted(classcount.items(),key=op.itemgetter(1),reverse=True)
    return sortedclasscount[0][0]

# testlist1=['a','a','b','c','d','c','a','e','a']
# print(majorityCnt(testlist1))

