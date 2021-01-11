import json
import os
import re
import time
from datetime import datetime

from django.shortcuts import render

# Create your views here.
from django.utils.encoding import escape_uri_path
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import StreamingHttpResponse

from djangoProject import settings
from reports.models import Reports
from reports.serializers import RepoetsModelSerializer
from reports.utils import format_output, get_file_contents


class ReportsViewSet(ModelViewSet):
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
    queryset = Reports.objects.filter(is_delete=False)
    serializer_class = RepoetsModelSerializer
    # 指定需要排序的字段
    ordering_fields = ['name', 'id']
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance: Reports):
        instance.is_delete = True
        instance.save()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['results'] = format_output(response.data['results'])
        return response

    @action(methods=['get'], detail=True)
    def download(self, request, pk=None):
        instance = self.get_object()
        html = instance.html
        name = instance.name
        mtch = re.match(r'(.*_)\d+', name)
        if mtch:
            mtch = mtch.group(1)
            report_filename = mtch + time.strftime('%Y%m%d%H%M%S', time.localtime()) + '.html'
        else:
            report_filename = name
        report_path = os.path.join(settings.REPORTS_DIR, report_filename)
        with open(report_path, 'w+', encoding='utf-8') as one_file:
            one_file.write(html)
        response = StreamingHttpResponse(get_file_contents(report_path))
        report_path_final = escape_uri_path(report_filename)
        response['Content-Type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(report_path_final)
        return response

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        datas = serializer.data
        try:
            datas['summary'] = json.loads(datas['summary'], encoding='utf-8')
        except Exception as e:
            pass
        return Response(datas)
