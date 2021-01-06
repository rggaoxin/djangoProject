from django.urls import path, include
from projects import views
from rest_framework import routers

# 创建路由对象
router = routers.SimpleRouter()
# router = routers.DefaultRouter()
# 注册路由
# prefix为路由前缀，一般添加为应用名即可
# viewset为视图集
router.register(r'projects', views.ProjectsViewSet)

urlpatterns = [
    # path('indexview/<int:pk>/', views.IndexView.as_view()),  # int为路径参数类型转化器，：左边为转换器，右边为参数别名，int、slog、uuid
    # path('projects/', views.ProjectsList.as_view()),
    # path('projects/<int:pk>/', views.ProjectsDetail.as_view()),
    # path('projects/', views.ProjectsViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create',
    # }), name='projects-list'),
    # path('projects/<int:pk>/', views.ProjectsViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # }), name='projects-list'),
    # path('projects/names/', views.ProjectsViewSet.as_view({
    #     'get': 'names',
    # }), name='projects-names'),
    # path('projects/<int:pk>/interfaces/', views.ProjectsViewSet.as_view({
    #     'get': 'interfaces',
    # }), name='interfaces'),
    # 将自动生成的路由，添加到urlpatterns中
    # path('', include(router.urls))
]

urlpatterns += router.urls
