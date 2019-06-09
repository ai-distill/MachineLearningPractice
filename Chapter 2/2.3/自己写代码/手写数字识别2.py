import os
import numpy as np


def img2Vec(imgFile):
    vector = np.zeros((1, 1024))
    with open(imgFile, 'r') as f:
        content = f.readlines()
        line_number = len(content)
        for line_num in range(line_number):
            content_line = content[line_num].strip()
            len_content_line = len(content_line)
            for line in range(len_content_line):
                vector[0, line_num*32 + line] = content_line[line]
    return vector


def init_data(trainDataFilePath):
    """
    将训练数据集文件夹中所有数据加入的数据集
    :param trainDataFilePath: 训练数据集文件夹
    :return: 返回dataset以及对应的标签
    """
    train_data_files = os.listdir(trainDataFilePath)
    len_train_data_files = len(train_data_files)
    dataset = np.zeros((len(train_data_files), 1024))
    labels = []
    for index in range(len_train_data_files):
        labels.append(int(train_data_files[index][0]))
    return dataset, labels


def kNNClassify(imgFile, dataset, k):
    vector = img2Vec(imgFile)
    distances = []
    print(dataset.shape)
    for index in range(dataset.shape[0]):
        print(dataset[index])
        distances.append(np.sqrt(np.sum(np.square(vector-dataset[index]))))
    print(len(distances))
    print(distances)
    sorted_distances = np.array(distances).argsort()
    sorted_distances = sorted_distances[0:k]
    print(sorted_distances)
    count = {}
    for i in range(len(sorted_distances)):
        if sorted_distances[i] in count.keys():
            count[labels[sorted_distances[i]]] += 1
        else:
            count[labels[sorted_distances[i]]] = 1
    count = sorted(count.items(), key=lambda x:x[1])
    print(count)
    print(len(labels))
    return labels[count[-1][0]]


if __name__ == '__main__':
    dataset, labels = init_data('../trainingDigits')
    print(kNNClassify('../trainingDigits/3_99.txt', dataset, 10))
    # array = [1, 2, 3]
    # array = np.array(array)
    # array.argsort()
    # distances = {1: 1.5, 2: 3.5, 3: 1.9}
    # distances = sorted(distances.items(), key=lambda x: x[1])
    # print(distances)
    # print(distances.count(1.5))

# print(img2Vec('../testDigits/0_0.txt'))
# print(init_data('../trainingDigits'))

# vector = np.array([1, 2, 3])
# dataset = np.array([[1, 2, 2,], [4, 5, 6]])
# print(np.sqrt(np.sum(np.square(vector-dataset[1]))))
