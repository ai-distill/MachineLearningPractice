# 导入科学计算包
from numpy import *
# 导入运算符模块，k近邻算法执行排序操作时将会使用这个模块提供的函数
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels
