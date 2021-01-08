import re

from django.db.models import Count

from interfaces.models import Interfaces
from testsuits.models import Testsuites


def get_count_by_project(datas):
    datas_list = []
    for item in datas:
        mtch = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        item['create_time'] = mtch.group(1) + ' ' + mtch.group(2)
        project_id = item['id']
        interfaces_count = Interfaces.objects.filter(project_id=project_id, is_delete=False).count()
        """
        sql语句：
        SELECT `tb_interfaces`.`id`, COUNT(`tb_testcases`.`id`) AS `testcase` FROM `tb_interfaces` LEFT OUTER JOIN 
        `tb_testcases` ON (`tb_interfaces`.`id` = `tb_testcases`.`interface_id`) WHERE 
        (NOT `tb_interfaces`.`is_delete` AND `tb_interfaces`.`project_id` = 4) GROUP BY `tb_interfaces`.`id` 
        ORDER BY NULL
        """
        interface_testcase_objs = Interfaces.objects.values('id').annotate(testcase=Count('testcases'))\
            .filter(project_id=project_id, is_delete=False)
        testcases_count = 0
        for one_dict in interface_testcase_objs:
            testcases_count += one_dict['testcase']
        interface_configures_objs = Interfaces.objects.values('id').annotate(configure=Count('configures'))\
            .filter(project_id=project_id, is_delete=False)
        configures_count = 0
        for one_dict in interface_configures_objs:
            configures_count += one_dict['configure']
        testsuits_count = Testsuites.objects.filter(project_id=project_id, is_delete=False).count()
        item['interfaces'] = interfaces_count
        item['testcases'] = testcases_count
        item['testsuits'] = testsuits_count
        item['configures'] = configures_count
        datas_list.append(item)
    return datas_list
