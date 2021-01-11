from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from interfaces.serializers import *
# ViewSet不在支持get、post、put、delete等请求方法，二只支持action动作，如list、retrieve等
# 但是ViewSet中未提供get_object()/get_serializer()等方法
# 所以需要继承GenericViewSet
from interfaces.utils import *


class InterfacesViewSet(viewsets.ModelViewSet):
    """
    create:
    创建接口信息

    list:
    显示所有接口信息

    retrieve:
    返回接口（单个）详情数据

    update：
    更新（全）接口

    partial_update:
    更新（部分）接口

    destroy:
    删除接口

    names:
    返回所有接口ID和名称

    """
    permission_classes = [permissions.IsAuthenticated]

    # 指定查询集
    queryset = Interfaces.objects.filter(is_delete=False)
    # 指定序列化器
    serializer_class = InterfaceModelSerializer
    # 指定需要排序的字段
    ordering_fields = ['name', 'id']

    def perform_destroy(self, instance: Interfaces):
        instance.is_delete = True
        instance.save()

    # 可以使用action装饰器来申明自定义的动作
    # 默认情况下，实例方法名就是动作名
    # methods参数用于指定该动作支持的请求方法，默认为get
    # detail参数用于指定该动作要处理的是否为详情资源对象（url是否需要传递pk值），详情数据，返回多条数据设为false，单条数据为true
    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = InterfaceModelSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['results'] = get_count_by_project(response.data['results'])
        return response

    @action(methods=['get'], detail=True)
    def testcases(self, request, pk=None):
        testcase_objs = Testcases.objects.filter(interface_id=pk, is_delete=False)
        one_list = []
        for obj in testcase_objs:
            one_list.append({
                'id': obj.id,
                'name': obj.name
            })
        return Response(data=one_list)

    @action(methods=['get'], detail=True, url_path='configs')
    def configures(self, request, pk=None):
        configures_objs = Configures.objects.filter(interface_id=pk, is_delete=False)
        one_list = []
        for obj in configures_objs:
            one_list.append({
                'id': obj.id,
                'name': obj.name
            })
        return Response(data=one_list)
