from numpy import *

# 生成4个数据组成的ndarray
num = random.rand(4)
print(num)
print(type(num))
# 生成4行4列数据组成的ndarray
number = random.rand(4, 4)
print(number)
print(type(number))

# 将number转换成一个矩阵
number_matrix = mat(number)
print(number_matrix)
print(type(number_matrix))
# .I操作符实现矩阵求逆的运算
invRandMat = number_matrix.I
print(invRandMat * number_matrix)

# 创建4 * 4的单位矩阵
print(eye(4))
