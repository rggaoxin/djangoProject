import re

from configures.models import Configures
from testcases.models import Testcases


def get_count_by_project(datas):
    datas_list = []
    for item in datas:
        create_time = item['create_time']
        date = create_time.split('T')[0]
        time = create_time.split('T')[1].split('+')[0].split('.')[0]
        item['create_time'] = date + ' ' + time
        interface_id = item['id']
        """
        sql语句：
        SELECT `tb_interfaces`.`id`, COUNT(`tb_testcases`.`id`) AS `testcase` FROM `tb_interfaces` LEFT OUTER JOIN 
        `tb_testcases` ON (`tb_interfaces`.`id` = `tb_testcases`.`interface_id`) WHERE 
        (NOT `tb_interfaces`.`is_delete` AND `tb_interfaces`.`project_id` = 4) GROUP BY `tb_interfaces`.`id` 
        ORDER BY NULL
        """
        testcases_count = Testcases.objects.filter(interface_id=interface_id, is_delete=False).count()
        configures_count = Configures.objects.filter(interface_id=interface_id, is_delete=False).count()
        item['testcases'] = testcases_count
        item['configures'] = configures_count
        datas_list.append(item)
    return datas_list
