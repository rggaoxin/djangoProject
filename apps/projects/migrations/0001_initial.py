# Generated by Django 3.1.3 on 2021-01-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, help_text='更新时间', verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, help_text='逻辑删除', verbose_name='逻辑删除')),
                ('id', models.AutoField(help_text='id主键', primary_key=True, serialize=False, verbose_name='id主键')),
                ('name', models.CharField(help_text='项目名称', max_length=200, unique=True, verbose_name='项目名称')),
                ('leader', models.CharField(help_text='项目经理', max_length=30, verbose_name='项目经理')),
                ('tester', models.CharField(help_text='项目测试人员', max_length=30, verbose_name='项目测试人员')),
                ('programmer', models.CharField(default='小白', help_text='开发人员', max_length=30, verbose_name='开发人员')),
                ('publish_app', models.CharField(default='发布软件', help_text='发布用户名', max_length=30, verbose_name='发布用户名')),
                ('desc', models.CharField(blank=True, default='', help_text='简要描述', max_length=255, null=True, verbose_name='简要描述')),
            ],
            options={
                'verbose_name': '项目信息',
                'verbose_name_plural': '项目信息',
                'db_table': 'tb_projects',
            },
        ),
    ]
