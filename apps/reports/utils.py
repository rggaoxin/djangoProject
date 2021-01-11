import re

from configures.models import Configures
from testcases.models import Testcases


def format_output(datas):
    datas_list = []
    for item in datas:
        result = 'Pass' if item['result'] else 'Fail'
        mtch = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        item['create_time'] = mtch.group(1) + ' ' + mtch.group(2)
        item['result'] = result
        datas_list.append(item)
    return datas_list


def get_file_contents(filename, chunk_size=512):
    """
    文件生成器,防止文件过大，导致内存溢出
    :param filename: 文件绝对路径
    :param chunk_size: 块大小
    :return: 生成器
    """
    with open(filename, mode='rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break
