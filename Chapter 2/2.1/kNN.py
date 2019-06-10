# 导入科学计算模块Numpy
from numpy import *
# 导入运算符模块：k近邻执行排序操作的时候将会使用这个模块
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify(inX, dataSet, labels, k):
    """
    k近邻算法的实现
    :param inX: 输入向量
    :param dataSet: 输入的训练样本集
    :param labels:  标签向量
    :param k:   选择最近邻居的数目
    :return:    返回k近邻算法执行后分类的结果
    """
    dataSetSize = dataSet.shape[0]

    # 进行距离计算
    ## 将其扩展为与标签个数相同的输入数据的矩阵，执行矩阵减操作时，直接对每个对应的元素互相减去
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5

    # 进行统计
    sortedDistIndicies = distances.argsort()
    classCount = {}

    # 选择距离最小的k个点
    for i in range(k):
        votellabel = labels[sortedDistIndicies[i]]
        classCount[votellabel] = classCount.get(votellabel, 0) + 1

    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


