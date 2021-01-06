from rest_framework import serializers

from interfaces.models import Interfaces
from projects.models import Projects
from debugtalks.models import DebugTalks
from interfaces.models import Interfaces


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        # 指定参考哪一个模型类来创建
        model = Projects
        # 指定为模型类的哪些字段来生成序列化器
        # fields = "__all__"
        # 指定部分字段
        # fields = ('id', 'name', 'leader', 'tester', 'progarmer')
        # 排除部分字段
        exclude = ('update_time', 'is_delete')
        # 限制字段为可读，不可写
        # read_only_fields = ('leader', 'tester')
        extra_kwargs = {
            'create_time': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        project_obj = super(ProjectModelSerializer, self).create(validated_data)
        DebugTalks.objects.create(project=project_obj)
        return project_obj


class ProjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        medel = Projects
        fields = ('id', 'name')


class InterfaceNameSerializer(serializers.ModelSerializer):
    class Meta:
        medel = Interfaces
        fields = ('id', 'name', 'tester')


class InterfacesByProjectIdserializer(serializers.ModelSerializer):
    interfaces_set = InterfaceNameSerializer(read_only=True, many=True)

    class Meta:
        medel = Projects
        fields = ('id', 'interfaces_set')
