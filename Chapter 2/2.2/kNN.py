# 导入科学计算包
from numpy import *
# 导入运算符模块，k近邻算法执行排序操作时将会使用这个模块提供的函数
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify(inX, dataSet, labels, k):
    """
    根据欧式距离公式计算出的距离从小到大排序，返回前k个元素
    :param inX: 用于分类的输入向量
    :param dataSet: 输入的训练样本集
    :param labels: 标签向量
    :param k: 标签向量元素的个数或训练集中数据的行数
    :return:
    """
    dataSetSize = dataSet.shape[0]
    # 距离计算
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    # 以下两行，选择距离最小的k个点
    for i in range(k):
        votellabel = labels[sortedDistIndicies[i]]
        classCount[votellabel] = classCount.get(votellabel, 0) + 1
        sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    arrayOlines = fr.readlines()
    numberOfLines = len(array(arrayOlines))
    # 得到文件行数
    returnMat = zeros((numberOfLines, 3))
    # 创建返回的Numpy矩阵
    classLabelVector = []
    index = 0
    # 解析文件数据到列表
    for line in arrayOlines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


def autoNorm(dataSet):
    """
    将数据集特征值归一化以避免差距大的特征带来的影响
    :param dataSet:
    :return:
    """
    minVals = dataSet.min()
    maxVals = dataSet.max()
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def datingClassTest():
    """
    分类器测试代码
    :return: 返回错误率
    """
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("The classifier came back: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if classifierResult != datingDataMat[i]:
            errorCount += 1.0
    print("the total error rate is: %f " % (errorCount / float(numTestVecs)))


def classifyPerson():
    """
    约会网站预测函数
    :return: None
    """
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input("percentage of the time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify((inArr - minVals) / ranges, normMat, datingLabels, 3)
    print("You will probably like this person: ", resultList[classifierResult - 1])



print(datingClassTest())
