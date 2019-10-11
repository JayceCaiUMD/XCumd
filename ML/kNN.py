import numpy as np
import operator

"""说明:
输入的训练集和测试集都应该是ndarray对象，且最后一列为label
"""
def creatDataSet():
    dataset = np.array([[1.0, 1.1, 'A'], [1.0, 1.0, 'A'], [0, 0, 'B'], [0, 0.1, 'B']])
    return dataset


def classify(inX, dataSet, k):  # 测试集，训练集
    dataSetSize = dataSet.shape[0]
    data = inX[:-1].astype('f')  # .shape --return (rows,columns)
    diffMat = np.tile(data, (dataSetSize, 1)) - dataSet[:, :-1].astype('f')  # .tile( data,(dataset,1)) 和训练集每一个特征对应相减
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1)
    distance = sqDistance ** 0.5
    sortedDistIndices = distance.argsort()  # 返回各个位置排序的索引，升序
    labels = dataSet[:, -1]
    classcount = {}
    for i in range(k):
        votelabel = labels[sortedDistIndices[i]]
        classcount[votelabel] = classcount.get(votelabel, 0) + 1  # 返回指定key的值，不存在则创建为0
    sortedClassCount = sorted(classcount.items(), key=operator.itemgetter(1), reverse=True)  # 按频率给字典排序，降序
    return sortedClassCount[0][0]  # 返回计数最多的类


def file2matrix(filename):
    fr = open(filename)
    arrayOlines = fr.readlines()  # 返回全部行
    # numberOfLines = len(arrayOlines)
    # returnMat = np.zeros((numberOfLines, 3))  # n行3列的零矩阵
    matrix = []
    label = []
    for line in arrayOlines:
        line = line.strip()
        listFromline = line.split('\t')
        matrix.append(listFromline)
        dmatrix = np.array(matrix)
        # classLabelVetor.append(listFromline[-1])  # 将字符串或者数字装换成整数
    return dmatrix  # 返回整理好的数据集,最后一列是label


def autoNorm(dataSet):  # 计量单位归一化
    datat = dataSet[:, :-1].astype('f')  # 除去最后一列标签，都导入
    minVals = datat.min(0)  # 每列的最小值
    maxVals = datat.max(0)
    ranges = maxVals - minVals
    m = datat.shape[0]
    datat = datat - np.tile(minVals, (m, 1))
    datat = datat / np.tile(ranges, (m, 1))
    dataSet[:, :-1] = datat
    return dataSet


def classifier(trainset, testset, k):
    testsetSize = len(testset)
    errorn = 0
    row = 0
    for n in testset:
        pridLabel = classify(n, trainset, k)
        if pridLabel != testset[row, -1]:
            errorn += 1
        row += 1
    erate = errorn / len(testset)
    return erate, testsetSize


def bootstrap(dataset):
    sample = []
    for n in range(len(dataset)):
        sample.append(dataset[np.random.randint(0, len(dataset))])
    return np.array(sample)
