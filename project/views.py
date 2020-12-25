from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.views import View
import json
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework import mixins
from utils.pagination import PageNumberPaginationManual
from .models import *
from django.db.models import Q
from project.serializer import *


def index(request):
    """
    函数视图
    index视图
    """
    if request.method == 'GET':
        return HttpResponse("<h1>GET请求：Hello World!</h1>")
    elif request.method == 'POST':
        return HttpResponse("<h1>POST请求：Hello World!</h1>")
    else:
        return HttpResponse("<h1>其他请求：Hello World!</h1>")
    # return JsonResponse({'message': '请求成功'})


"""类视图"""


class IndexView(View):
    def get(self, request):
        # 创建数据
        # 方法一
        # one_obj = Projects(name='这是一个牛逼的项目11111', leader='icon', programer='若影', publish_app='这是一个厉害的应用', desc="描述")
        # one_obj.save()
        # 方法二
        # Projects.objects.create(name='这是一个牛逼的项目111', leader='icon', programer='若影', publish_app='这是一个厉害的应用', desc="描述")

        # 获取数据
        # QuerySet查询集，相当于一个列表，存放所有项目的列表
        # 获取所有数据
        # infos = Projects.objects.all()
        # for i in infos:
        #     print(i.name)
        # 获取指定数据,唯一值
        # one_project = Projects.objects.get(id=1)
        # print(one_project.name)
        # 获取多个值用filter/exclude(NOT)
        # project = Projects.objects.filter(leader='icon')
        # project = Projects.objects.exclude(leader='icon')
        # print(project.all())
        # print(project[1])
        # 模糊查询 __contains包含 __icontains忽略大小写 in后面需要跟列表
        # project = Projects.objects.filter(leader__icontains='icon')
        # print(project.all())
        # project1 = Projects.objects.filter(leader__contains='icon')
        # print(project1.all())
        # project2 = Projects.objects.filter(leader__in=['icon', ''])
        # print(project2.all())
        # 关联查询 外键字段  __从表的字段名__contains
        # qs = Projects.objects.filter(interfaces__name='登录接口')
        # print(qs.all())
        # id__gt大于
        # qs = Projects.objects.filter(id__gt=2)
        # print(qs.all())
        # 多个条件 filter(leader='icon', name__contains='牛逼')与
        # qs = Projects.objects.filter(leader='icon', name__contains='牛逼')
        # print(qs.all())
        # 多个条件 filter(leader='icon', name__contains='牛逼')或
        # qs = Projects.objects.filter(Q(leader='icon') | Q(name__contains='牛逼'))
        # print(qs.all())
        # 多个条件拼接查询，相当于and
        # qs = Projects.objects.filter(Q(leader='icon') | Q(name__contains='牛逼'))
        # qqq = qs.filter(leader='icon')
        # print(qqq.all())
        # 修改需要先获取到需要修改的模型对象，然后修改，保存
        # one_project = Projects.objects.get(id=1)
        # one_project.leader = '搞搞'
        # one_project.save()
        # 删除需要先获取到需要修改的模型对象，然后删除
        # one_project = Projects.objects.get(id=7)
        # one_project.delete()

        # 排序
        # qs = Projects.objects.filter(id_gt=3).order_by('name')
        # print(qs)
        return JsonResponse({'msg': 'success'})
        # return render(request, 'demo.html')

    def post(self, request):
        return HttpResponse("<h1>POST请求：Hello World!</h1>")

    # def post(self, request):
    #     return HttpResponse("<h1>POST请求：Hello World!</h1>")
    # body = request.body.decode('utf-8')
    # return JsonResponse(json.loads(body))

    def put(self, request):
        return HttpResponse("<h1>PUT请求：Hello World!</h1>")


class ProjectsList(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    # 指定查询集
    queryset = Projects.objects.all()
    # 指定序列化器
    serializer_class = ProjectModelSerializer
    # 在视图类中指定过滤引擎
    # filter_backends = [filters.OrderingFilter]
    # 指定需要排序的字段
    ordering_fields = ['name', 'leader']
    # 在类视图中指定过滤引擎
    filter_backends = [DjangoFilterBackend]
    # 指定需要过滤的字段
    filterset_fields = ['name', 'leader', 'tester']

    # 单独指定分页类
    # paginaton_class = PageNumberPaginationManual

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        # 获取查询集
        # project_qs = self.get_queryset()
        # 使用filter_queryset方法过滤查询
        # project_qs = self.filter_queryset(self.get_queryset())
        # # 使用paginate_queryset进行分页，返回查询集
        # page = self.paginate_queryset(project_qs)
        # if page is not None:
        #     serializer = self.get_serializer(instance=page, many=True)
        #     return self.get_paginated_response(serializer.data)
        # else:
        #     project_serializer = self.get_serializer(instance=project_qs, many=True)
        #     return JsonResponse(project_serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        # project_name = request.project_name
        # 1.校验前端传参
        # json_data = request.body.decode('utf-8')
        # python_data = json.loads(json_data, encoding='utf-8')
        # serialazer = ProjectModelSerializer(data=python_data)
        # # serialazer.is_valid()开始校验参数填入是否符合序列器的标准
        # try:
        #     serialazer.is_valid(raise_exception=True)
        #     # 如果在创建序列化器对象的时候，只给data传参，那么调用save（）方法，实际调用的就是序列化器对象的create方法
        #     serialazer.save()
        #     return JsonResponse(serialazer.data, safe=False)
        # except:
        #     return JsonResponse(serialazer.errors)


# class ProjectsDetail(View):
#     def get_object(self, pk):
#         try:
#             return Projects.objects.get(id=pk)
#         except Projects.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         try:
#             project = self.get_object(pk)
#             # 通过模型类对象（或者查询集），传给instance可进行序列化操作
#             project_serializer = ProjectModelSerializer(instance=project)
#             return JsonResponse(project_serializer.data)
#         except:
#             return Http404
#
#     def put(self, request, pk):
#         project = self.get_object(pk)
#         json_data = request.body.decode('utf-8')
#         python_data = json.loads(json_data, encoding='utf-8')
#         serializer = ProjectModelSerializer(data=python_data, instance=project)
#         try:
#             serializer.is_valid(raise_exception=True)
#             # 在创建序列化器对象时，如果同时给instance和data传参，那么调用save方法，会自动调用序列化器对象的update
#             serializer.save()
#             return JsonResponse(serializer.data)
#         except:
#             return JsonResponse(serializer.errors)
#
#     def delete(self, request, pk):
#         project = self.get_object(pk)
#         project.delete()
#         return JsonResponse(None)


class ProjectsDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericAPIView, mixins.DestroyModelMixin):
    # 指定查询集
    queryset = Projects.objects.all()
    # 指定序列化器
    serializer_class = ProjectModelSerializer
    # 在视图类中指定过滤引擎
    filter_backends = [filters.OrderingFilter]
    # 指定需要排序的字段
    ordering_fields = ['name', 'leader']

    # 使用lookup_field类属性，可以修改主键路由名称
    # 传参为pk则不需要这行代码
    # lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        # # 无需自定义get_object()方法
        # project = self.get_object()
        # # 使用get_serializer获取序列化器类
        # serializer = self.get_serializer(instance=project)
        # # 通过模型类对象（或者查询集），传给instance可进行序列化操作
        # # serializer = ProjectModelSerializer(instance=project)
        # return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)
        # project = self.get_object()
        # serializer = self.get_serializer(data=project, instance=project)
        # try:
        #     serializer.is_valid(raise_exception=True)
        #     # 在创建序列化器对象时，如果同时给instance和data传参，那么调用save方法，会自动调用序列化器对象的update
        #     serializer.save()
        #     return Response(serializer.data, status=HTTP_201_CREATED)
        # except:
        #     return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        # project = self.get_object()
        # # serializer = self.get_serializer(data=project,instance=project)
        # project.delete()
        # # serializer.delete()
        # return Response(None, status=204)
