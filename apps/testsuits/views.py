from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from testsuits.utils import format_output
from testsuits.models import *
from testsuits.serializers import *


class TestsuitsViewSet(viewsets.ModelViewSet):
    """
    list:
    返回测试报告（多个）列表数据

    create:
    创建测试报告

    retrieve:
    返回测试报告（单个）详情数据

    update:
    更新测试报告

    partial_update:
    更新（部分）测试报告

    destroy:
    删除测试报告

    """
    queryset = Testsuites.objects.filter(is_delete=False)
    serializer_class = TestsuitsSerializer
    # 指定需要排序的字段
    ordering_fields = ['name', 'id']
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance: Testsuites):
        instance.is_delete = True
        instance.save()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['results'] = format_output(response.data['results'])
        return response

    def update(self, request, pk=None, *args, **kwargs):
        instance = Testsuites.objects.filter(is_delete=False, id=pk)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)