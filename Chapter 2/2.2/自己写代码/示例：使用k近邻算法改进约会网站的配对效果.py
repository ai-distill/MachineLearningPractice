'''
数据文件解析：
1. 每年获得的飞行常客里程数
2. 玩视频游戏所耗时间百分比
3. 每周消费的冰淇淋公升数
'''

DATA_PATH = '../datingTestSet2.txt'


def init_data():
    """
    对输入数据进行处理
    :return:    users 数据处理之后的用户特征值数据集
                label 标签对应的数据集
    """
    # 用户三个特征对应的数据
    users = []
    # 用户对应的标签数据集
    label = []
    with open(DATA_PATH, 'r') as f:
        data_lines = f.readlines()
        for line in data_lines:
            line_content = line.strip().split('\t')
            label.append(int(line_content[-1]))
            users.append(line_content[0:3])
    return users, label


import matplotlib.pyplot as plt

def analy_data():
    """
    对数据进行分析
    :return:
    """
    fig = plt.figure()
    users, label = init_data()
    for user in users:
        line_num =
    img1 = plt.subplot(311)
    plt.scatter(users[0], marker='o')
    img2 = plt.subplot(312, )
    plt.scatter()
    img3 = plt.subplot(313, )
    plt.show()

print(init_data())
