from rest_framework import serializers
from project.models import Projects

# 1.集成Serializer类或者子类
from rest_framework.validators import UniqueValidator


def is_unique_project_name(name):
    """自定义校验器"""
    if '项目' not in name:
        raise serializers.ValidationError('项目名称必须“项目”')


class ProjectSerializer(serializers.Serializer):
    """
    创建项目序列化器类
    """
    # label选项相当于verbose_name
    # read_only=True指定该字段只能作为序列化输出
    # 定义的序列化器的字段默认既可以进行序列化输出，也可以进行反序列化输入
    # write_only=True指定该字段只能作为反序列化输入
    id = serializers.IntegerField(label='ID', read_only=True)
    # validators校验器
    name = serializers.CharField(max_length=200, label='项目名称', help_text='项目名称',
                                 validators=[UniqueValidator(queryset=Projects.objects.all(), message='项目名不能重复'),
                                             is_unique_project_name],
                                 error_messages={'max_length': '长度不能超过200'})
    leader = serializers.CharField(max_length=50, min_length=6, label='负责人', help_text='负责人',
                                   error_messages={'max_length': '长度不能超过50',
                                                   'min_length': '长度不能少于6'})
    tester = serializers.CharField(max_length=50, label='测试人员', help_text='测试人员')
    programer = serializers.CharField(max_length=50, label='开发人员', help_text='开发人员')
    publish_app = serializers.CharField(max_length=100, label='发布应用', help_text='发布应用')
    # allow_null相当于模型类中的null=True表示该字段可以为空，allow_blank相当于模型类中的blank=True可以设置该字段前端可以不传，default设置默认值
    desc = serializers.CharField(label='简要描述', help_text='简要描述', allow_blank=True, default='', allow_null=True)

    # 单字段校验,函数名格式固定，前面为validate_，后面加上字段名称name
    # 字段校验器的顺序，按照name校验器中的顺序校验，交验完最后校验该方法
    # 字段定义时的显示（包括validators列表条目从左到右进行校验）---单字段的校验（validate_字段名）
    def validate_name(self, value):
        if not value.endswith('项目'):
            raise serializers.ValidationError('项目名称必须以”项目结尾“')
        return value

    # 多字段联合校验
    def validate(self, attrs):
        if 'icon' not in attrs['tester'] and 'icon' not in attrs['leader']:
            raise serializers.ValidationError('icon必须是项目负责人或者测试人员')
        else:
            return attrs

    def create(self, validated_data):
        return Projects.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.leader = validated_data['leader']
        instance.tester = validated_data['tester']
        instance.programer = validated_data['programer']
        instance.publish_app = validated_data['publish_app']
        instance.desc = validated_data['desc']
        instance.save()
        return instance


class ProjectModelSerializer(serializers.ModelSerializer):
    # 手动序列化字段
    # name = serializers.CharField(max_length=200, label='项目名称', help_text='项目名称',
    #                              validators=[UniqueValidator(queryset=Projects.objects.all(), message='项目名不能重复'),
    #                                          is_unique_project_name],
    #                              error_messages={'max_length': '长度不能超过200'})

    class Meta:
        # 指定参考哪一个模型类来创建
        model = Projects
        # 指定为模型类的哪些字段来生成序列化器
        fields = "__all__"
        # 指定部分字段
        # fields = ('id', 'name', 'leader', 'tester', 'progarmer')
        # 排除部分字段
        # exclude = ('publish_app','desc')
        # 限制字段为可读，不可写
        # read_only_fields = ('leader', 'tester')
        # extra_kwargs = {
        #     'leader': {
        #         'write_only': True,
        #         'error_messages': {'max_length': '最大长度不超过50'}
        #     }
        # }

    def validate_name(self, value):
        if not value.endswith('项目'):
            raise serializers.ValidationError('项目名称必须以”项目结尾“')
        return value

    # 多字段联合校验
    def validate(self, attrs):
        if 'icon' not in attrs['tester'] and 'icon' not in attrs['leader']:
            raise serializers.ValidationError('icon必须是项目负责人或者测试人员')
        else:
            return attrs
