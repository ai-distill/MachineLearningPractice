import numpy as np
import matplotlib.pyplot as plt

def file2matrix(filename):
    labels = []
    with open(filename) as f:
        data = f.readlines()
        numberOfLines = len(data)
        returnMat = np.zeros((numberOfLines, 3))
        for index in range(numberOfLines):
            line = data[index].strip()
            content_line = line.split('\t')
            labels.append(content_line[-1])
            returnMat[index, :] = content_line[0:3]
    return returnMat, labels


matrix, labels = file2matrix('../datingTestSet2.txt')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(matrix[:, 1], matrix[:, 2], 15.0*np.array(), 15.0*np.array())
plt.show()
