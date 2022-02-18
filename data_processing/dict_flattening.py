# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

def dict_flattening(dis_dict, separator='_'):
    # 字典扁平化处理
    prefix = ""
    dict_ = {}

    def traversal_dict(dis, prefix_k, separator_k):
        for i, j in dis.items():
            if isinstance(j, dict):
                traversal_dict(j, prefix_k + i + separator_k, separator_k)
            else:
                dict_[prefix_k + i] = j

    traversal_dict(dis_dict, prefix, separator)
    return dict_


if __name__ == '__main__':
    test_dict = {
        'a': 1,
        'b': {'β': 2}
    }
    print(f'原始字典：{test_dict}')
    print(f'字典扁平化：{dict_flattening(test_dict)}')

