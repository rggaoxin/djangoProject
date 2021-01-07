from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from projects.serializer import *


# ViewSet不在支持get、post、put、delete等请求方法，二只支持action动作，如list、retrieve等
# 但是ViewSet中未提供get_object()/get_serializer()等方法
# 所以需要继承GenericViewSet
class ProjectsViewSet(viewsets.ModelViewSet):
    """
    create:
    创建项目信息

    list:
    显示所有项目信息

    retrieve:
    返回项目（单个）详情数据

    update：
    更新（全）项目

    partial_update:
    更新（部分）项目

    destroy:
    删除项目

    names:
    返回所有项目ID和名称

    interfaces:返回某个项目的所有接口信息（ID和名称）
    """
    permission_classes = [permissions.IsAuthenticated]

    # 指定查询集
    queryset = Projects.objects.filter(is_delete=False)
    # 指定序列化器
    serializer_class = ProjectModelSerializer
    # 在视图类中指定过滤引擎
    # filter_backends = [filters.OrderingFilter]
    # 指定需要排序的字段
    ordering_fields = ['name', 'id']

    # 在类视图中指定过滤引擎
    # filter_backends = [DjangoFilterBackend]
    # 指定需要过滤的字段
    # filterset_fields = ['name', 'leader', 'tester']

    def perform_destroy(self, instance: Projects):
        instance.is_delete = True
        instance.save()

    # 可以使用action装饰器来申明自定义的动作
    # 默认情况下，实例方法名就是动作名
    # methods参数用于指定该动作支持的请求方法，默认为get
    # detail参数用于指定该动作要处理的是否为详情资源对象（url是否需要传递pk值），详情数据，返回多条数据设为false，单条数据为true
    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProjectNameSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    # 单独指定分页类
    # paginaton_class = PageNumberPaginationManual
    @action(methods=['get'], detail=True)
    def interfaces(self, request, pk=None):
        interface_objs = Interfaces.objects.filter(project_id=pk, is_delete=False)
        one_list = []
        for obj in interface_objs:
            one_list.append(
                {
                    'id': obj.id,
                    'name': obj.name
                }
            )
        return Response(data=one_list)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     page = self.paginate_queryset(queryset)
    #
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         datas = serializer.data
    #         datas = get_count_by_project(datas)
    #         return self.get_paginated_response(datas)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     datas = serializer.data
    #     datas = get_count_by_project(datas)
    #     return Response(datas)
