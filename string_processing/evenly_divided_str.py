# -*- coding: utf-8 -*-


def str_split1(string, copies_num):
    """
    按照指定的份数分割字符串。

    Args:
        string (str): 目标字符串
        copies_num (int): 份数
    Returns:
        分割后的字符串列表
    """
    fn = len(string) // copies_num
    rn = len(string) % copies_num
    ar = [fn + 1] * rn + [fn] * (copies_num - rn)
    si = [i * (fn + 1) if i < rn else (rn * (fn + 1) + (i - rn) * fn) for i in
          range(copies_num)]
    str_list = [string[si[i]:si[i] + ar[i]] for i in range(copies_num)]
    return str_list


def str_split2(string, copies_num):
    """
        按照指定的份数分割字符串。

        Args:
            string (str): 目标字符串
            copies_num (int): 份数
        Returns:
            分割后的字符串列表
        """
    fn = len(string) // copies_num
    rn = len(string) % copies_num
    str_list = []
    ix = 0
    for i in range(copies_num):
        if i < rn:
            str_list.append(string[ix:ix + fn + 1])
            ix += fn + 1
        else:
            str_list.append(string[ix:ix + fn])
            ix += fn
    return str_list


if __name__ == '__main__':
    s = 'abcdefghijklmnopqrstuvwxyz'
    print(str_split1(s, 5))
    print(str_split2(s, 5))
