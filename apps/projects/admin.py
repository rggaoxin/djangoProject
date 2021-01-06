from django.contrib import admin
from projects.models import Projects


# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
    """定值后台管理站点类"""
    # 指定在修改（新增）中需要显示的字段
    fields = ('name', 'leader', 'tester', 'programer', 'publish_app')
    list_display = ['id', 'name', 'leader', 'tester']


admin.site.register(Projects, ProjectsAdmin)
