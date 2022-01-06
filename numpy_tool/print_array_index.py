# -*- coding: utf-8 -*-
import numpy as np


def print_array_index(array):
    for v in array.flat:
        coordinate_list = []
        items_index = np.where(array == v)
        for index in range(array.ndim):
            coordinate_list.append(items_index[index][0])
        print(f'数组元素: {v:>2} {coordinate_list}')


if __name__ == '__main__':
    a = np.arange(12).reshape((2, 2, 3))
    print_array_index(a)
