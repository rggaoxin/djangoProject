def handle_env(datas):
    datas_list = []
    for item in datas:
        create_time = item['create_time']
        date = create_time.split('T')[0]
        time = create_time.split('T')[1].split('+')[0].split('.')[0]
        item['create_time'] = date + ' ' + time
        datas_list.append(item)
    return datas_list
