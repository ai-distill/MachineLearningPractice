from math import log
import operator


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter, reverse=True)
    return sortedClassCount


def calcShannonEnt(dataSet):
    """
    计算给定数据集的香农熵
    :param dataSet:
    :return:
    """
    numEntries = len(dataSet)
    labelCounts = {}

    # 以下五行：为所有可能分类创建字典
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
            labelCounts[currentLabel] += 1
        shannonEnt = 0.0

    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        print(prob)
        # 以2为底求对数
        shannonEnt -= prob * log(prob, 2)
    print(labelCounts)

    return shannonEnt


def createDataSet():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def splitDataSet(dataSet, axis, value):
    """
    按照给定特征划分数据集
    :param dataSet: 待划分的数据集
    :param axis: 划分数据集的特征
    :param value: 需要返回的特征值
    :return:
    """
    # 创建新的list对象
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            # 抽取
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    """
    选择最好的数据集划分方式
    :param dataSet: 对应的数据集
    :return: 返回最好的划分方式对应的特征
    """
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        # 以下两行 创建唯一的分类标签列表
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0

        # 以下五行 计算每种划分方式的信息熵
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy

        if (infoGain > bestInfoGain):
            # 计算最好的信息增益
            bestInfoGain = infoGain
            bestFeature = i
        return bestFeature


if __name__ == '__main__':
    myDat, labels = createDataSet()
    print(calcShannonEnt(dataSet=myDat))
    chooseBestFeatureToSplit(myDat)
    print(myDat)



