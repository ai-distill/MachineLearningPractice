import operator
from numpy import *
import os

def file2matrix(filename):
    """
    将文本记录转换为Numpy的解析程序
    :param filename:
    :return:
    """
    fr = open(filename)
    arrayOlines = fr.readlines()
    numberOfLines = len(arrayOlines)

    # 得到文件行数
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0

    # 以下三行用于解析文件到数据列表
    for line in arrayOlines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


# 分析数据
def plo():
    import matplotlib
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    datingDataMat, datingLabels = file2matrix('data/datingTestSet2.txt')
    # ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0*array(datingLabels), 15.0*array(datingLabels))
    plt.show()


def autoNorm(dataSet):
    # 传入一个0表示按照列取最小值
    minVals = dataSet.min(0)
    # 传入一个0表示按照列取最大值
    maxVals = dataSet.max(0)

    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    # 特征值相除
    normDataSet = normDataSet / tile(ranges, (m, 1))

    # Numpy中矩阵除法需要使用

    return normDataSet, ranges, minVals


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


def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('data/datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("The classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print("The total error rate is %f:" % (errorCount / float(numTestVecs)))


def img2vec(imgFile):
    """
    准备数据，将图像文件转换为1*1024的图像
    :param imgFile:
    :return:
    """
    vec = zeros((1, 1024))
    with open(imgFile) as f:
        content = f.readlines()
        line_number = len(content)
        for line_index in range(line_number):
            for index in range(len(content[line_index].strip())):
                vec[0, line_index*32 + index] = content[line_index].strip()[index]
    return vec


def handwritingClassTest():
    hwLabels = []
    trainingFileList = os.listdir('trainingDigits')

    # 获取目录内容
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        # 从文件名解析分类数字
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])

        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vec('trainingDigits/%s' % fileNameStr)
        testFileList = os.listdir('testDigits')
        errorCount = 0.0
        mTest = len(testFileList)

    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vec('testDigits/%s' % fileNameStr)
        classifierResult = classify(vectorUnderTest, trainingMat, hwLabels, 3)
        print('the classifier came back with: %d' % classNumStr)
        if (classifierResult != classNumStr):
            errorCount += 1.0
    print('the total number of errors is: %d' % errorCount)
    print('the total error rate is: %f' % (errorCount / float(mTest)))


if __name__ == '__main__':
    handwritingClassTest()
