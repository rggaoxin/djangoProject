import re


def get_count_by_project(datas):
    datas_list = []
    for item in datas:
        mtch = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        item['create_time'] = mtch.group(1) + ' ' + mtch.group(2)
        datas_list.append(item)
    return datas_list
