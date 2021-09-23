# -*- coding: utf-8 -*-
import json

import yaml


def yaml_file_to_json(src_path: str, dest_path: str = None):
    with open(src_path, 'r') as f:
        file_content = yaml.load(f, Loader=yaml.FullLoader)
    if not dest_path:
        json_content = json.dumps(file_content)
        print(json_content)
    else:
        with open(dest_path, 'w') as f:
            json.dump(file_content, f)


if __name__ == '__main__':
    yaml_file_to_json(
        'F:\D4-6bit_0707_1\D4-6bit_0707_1\qubit_data\q3_20210706_132725.yaml')
