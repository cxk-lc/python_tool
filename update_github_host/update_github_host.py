# -*- coding: utf-8 -*-
import os
import re

import requests
from bs4 import BeautifulSoup


def get_new_github_host():
    res = requests.get('https://gitee.com/doshengl/GitHub520')
    soup = BeautifulSoup(res.content, 'lxml')
    return soup.pre.get_text()


def update_hosts(new_github_host):
    f_path = r'C:\Windows\System32\drivers\etc'
    os.chdir(f_path)
    with open(os.path.join(f_path, 'hosts'), 'r') as f:
        f_content = f.read()
    if re.findall(r'# GitHub520[\s\S]*?End', f_content):
        print('更新 GitHub Hosts 配置')
        f_content = re.sub(r'# GitHub520[\s\S]*?End', new_github_host,
                           f_content)
        with open(os.path.join(f_path, 'hosts'), 'w') as f:
            f.write(f_content)
        print('更新完成！')
    else:
        print('添加 GitHub Hosts 配置')
        with open(os.path.join(f_path, 'hosts'), 'a+') as f:
            f.write(f'\n{new_github_host}')
        print('添加完成！')


if __name__ == '__main__':
    update_hosts(get_new_github_host())
