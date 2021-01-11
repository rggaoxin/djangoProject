from rest_framework import serializers

from interfaces.models import Interfaces
from projects.models import Projects


class InterfaceModelSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(help_text='项目名称')  # 外键
    project_id = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), help_text='项目id')

    class Meta:
        model = Interfaces
        exclude = ('update_time', 'is_delete')
        extra_kwargs = {
            'create_time': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        project = validated_data.pop('project_id')
        validated_data['project'] = project
        interface = Interfaces.objects.create(**validated_data)
        return interface

    def update(self, instance, validated_data):
        if 'project_id' in validated_data:
            project = validated_data.pop('project_id')
            validated_data['project'] = project
        return super().update(instance, validated_data)
