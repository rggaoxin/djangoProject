from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response

from debugtalks.serializers import *


class DebugtalksViewSet(viewsets.ReadOnlyModelViewSet, mixins.UpdateModelMixin):
    """
    list:
    返回debugtalk(多个列表数据)

    update:
    更新（全）debugtalk

    partial_updat:
    更新（部分）debugtalk
    """
    permission_classes = [permissions.IsAuthenticated]

    # 指定查询集
    queryset = DebugTalks.objects.filter(is_delete=False)
    # 指定序列化器
    serializer_class = DebugtalkModelSerializer
    # 指定需要排序的字段
    ordering_fields = ['name', 'id']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data_dict = {
            'id': instance.id,
            'debugtalk': instance.debugtalk
        }
        return Response(data_dict)