from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from envs.models import Envs
from envs.serializers import *
from envs.utils import handle_env


class EnvsViewSet(viewsets.ModelViewSet):
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
    queryset = Envs.objects.filter(is_delete=False)
    # 指定序列化器
    serializer_class = EnvsModelSerializer
    # 指定需要排序的字段
    ordering_fields = ['name', 'id']

    def perform_destroy(self, instance: Envs):
        instance.is_delete = True
        instance.save()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['result'] = handle_env(response.data['results'])
        return response

    @action(methods=['get'], detail=False)
    def names(self, request, pk=None):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'names':
            return EnvNameserializer
        else:
            return EnvsModelSerializer


class DebugtalksViewSet(object):
    pass