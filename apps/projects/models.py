from django.db import models
from utils.base_models import BaseModel


class Projects(BaseModel):
    """
    unique用于设置当前字段是否唯一，默认为False
    verbose_name用于设置更人性化的字段名
    help_text用于API文档的中文名称
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField(verbose_name='项目名称', max_length=200, help_text='项目名称')
    leader = models.CharField(verbose_name='项目经理', max_length=30, help_text='项目经理')
    tester = models.CharField(verbose_name='项目测试人员', max_length=30, help_text='项目测试人员')
    programmer = models.CharField(verbose_name='开发人员', max_length=30, help_text='开发人员', default='小白')
    publish_app = models.CharField(verbose_name='发布用户名', max_length=30, help_text='发布用户名', default='发布软件')
    desc = models.CharField(verbose_name='简要描述', max_length=255, help_text='简要描述', default='', null=True,
                            blank=True)

    class Meta:
        db_table = 'tb_projects'
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
