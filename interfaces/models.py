from django.db import models


# Create your models here.

class Interfaces(models.Model):
    """
    unique用于设置当前字段是否唯一，默认为False
    verbose_name用于设置更人性化的字段名
    help_text用于API文档的中文名称
    """
    name = models.CharField(max_length=200, verbose_name='接口名称', unique=True, help_text='接口名称')
    tester = models.CharField(max_length=50, verbose_name='测试人员', help_text='测试人员')
    # null=True表示该字段可以为空，blank=True可以设置该字段前端可以不传，default设置默认值
    desc = models.TextField(verbose_name='简要描述', help_text='简要描述', blank=True, default='', null=True)
    # models.IntegerField(choices=[''])
    # 第一个参数为关联的模型路径（应用名.模型类）或模型类，on_delete为当父表删除之后，该字段的处理方式，设置为models.CASCADE，则父表删除，字表也一起删除.
    """
    CASCADE:这就是默认的选项，级联删除，你无需显性指定它。
    PROTECT: 保护模式，如果采用该选项，删除的时候，会抛出ProtectedError错误。
    SET_NULL: 置空模式，删除的时候，外键字段被设置为空，前提就是blank=True, null=True,定义该字段的时候，允许为空。
    SET_DEFAULT: 置默认值，删除的时候，外键字段设置为默认值，所以定义外键的时候注意加上一个默认值。
    SET(): 自定义一个值，该值当然只能是对应的实体了
    """
    project = models.ForeignKey('project.Projects', on_delete=models.PROTECT, verbose_name='所属项目', help_text='所属项目')

    # 定义子类，用于设置当前数据模型的元数据信息
    class Meta:
        db_table = 'tb_interfaces'
        # 会在admin站点中显示该名称
        verbose_name = '接口'
        verbose_name_plural = '接口'
