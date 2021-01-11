from rest_framework import serializers

from debugtalks.models import *


# from projects.models import Projects


class DebugtalkModelSerializer(serializers.ModelSerializer):
    """
    DebugTalks序列化器
    """
    project = serializers.StringRelatedField(help_text='项目名称')

    class Meta:
        model = DebugTalks
        exclude = ('update_time', 'is_delete', 'create_time')
        extra_kwargs = {
            'name': {
                'read_only': True
            },
            'project': {
                'read_only': True
            },
            'debugtalk': {
                'write_only': True
            }
        }
