from django.db import models
from utils.base_models import BaseModel


class Interfaces(BaseModel):
    """
    unique用于设置当前字段是否唯一，默认为False
    verbose_name用于设置更人性化的字段名
    help_text用于API文档的中文名称
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField('接口名称', max_length=200, unique=True, help_text='接口名称')
    # 外键
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE,
                                related_name='interfaces', help_text='所属项目id')
    tester = models.CharField('测试人员', max_length=50, help_text='测试人员')
    desc = models.CharField(verbose_name='简要描述', max_length=255, help_text='简要描述', default='', null=True,
                            blank=True)

    # 定义子类，用于设置当前数据模型的元数据信息
    class Meta:
        db_table = 'tb_interfaces'
        verbose_name = '接口信息'
        verbose_name_plural = verbose_name
