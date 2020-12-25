from django.db import models


# Create your models here.


class Person(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    class Meta:
        # db_table = 'tb_projects'
        # 会在admin站点中显示该名称
        verbose_name = '人员'
        verbose_name_plural = '人员'



class Projects(models.Model):
    """
    unique用于设置当前字段是否唯一，默认为False
    verbose_name用于设置更人性化的字段名
    help_text用于API文档的中文名称
    """
    name = models.CharField(max_length=200, verbose_name='项目名称', unique=True, help_text='项目名称')
    leader = models.CharField(max_length=50, verbose_name='负责人', help_text='负责人')
    tester = models.CharField(max_length=50, verbose_name='测试人员', help_text='测试人员')
    programer = models.CharField(max_length=50, verbose_name='开发人员', help_text='开发人员')
    publish_app = models.CharField(max_length=100, verbose_name='发布应用', help_text='发布应用')
    # null=True表示该字段可以为空，blank=True可以设置该字段前端可以不传，default设置默认值
    desc = models.TextField(verbose_name='简要描述', help_text='简要描述', blank=True, default='', null=True)
    # models.IntegerField(choices=[''])

    # 定义子类，用于设置当前数据模型的元数据信息
    class Meta:
        db_table = 'tb_projects'
        # 会在admin站点中显示该名称
        verbose_name = '项目'
        verbose_name_plural = '项目'

    def __str__(self):
        return self.name
