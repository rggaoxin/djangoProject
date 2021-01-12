import re


def format_output(datas):
    datas_list = []
    for item in datas:
        mtch = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        item['create_time'] = mtch.group(1) + ' ' + mtch.group(2)
        mtch1 = re.search(r'(.*)T(.*)\..*?', item['update_time'])
        item['update_time'] = mtch1.group(1) + ' ' + mtch1.group(2)
        datas_list.append(item)
    return datas_list

