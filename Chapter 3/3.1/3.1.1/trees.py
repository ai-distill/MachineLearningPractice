from math import log


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





if __name__ == '__main__':
    myDat, labels = createDataSet()
    print(calcShannonEnt(dataSet=myDat))



