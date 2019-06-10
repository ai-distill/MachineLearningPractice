import numpy as np
import os


def img2vector(filename):
    vector = np.zeros((1, 1024))
    with open(filename, 'r') as f:
        content = f.readlines()
        for line_number in range(len(content)):
            for index in range(len(content[line_number].strip())):
                vector[0, line_number*32 + index] = int(content[line_number][index])
    return vector


def test():



if __name__ == '__main__':
    print(img2vector('../testDigits/0_0.txt'))