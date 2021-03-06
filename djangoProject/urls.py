"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions


# from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(
    openapi.Info(
        title="测试项目API",
        default_version='v1.0',
        description="测试工程接口文档",
        # terms_of_service="https://www.baidu.com",
        # contact=openapi.Contact(email="baidu@163.com"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # 权限类
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', index),
    path('', include('projects.urls')),
    path('', include('interfaces.urls')),
    path('', include('envs.urls')),
    # path('', include('configures.urls')),
    path('', include('debugtalks.urls')),
    path('', include('reports.urls')),
    # path('', include('testcases.urls')),
    path('', include('testsuits.urls')),
    path('', include('user.urls')),
    # path('docs/', include_docs_urls(title="测试平台接口文档", description="描述信息")),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/', include('rest_framework.urls')),
    path('user/', include('user.urls')),
]
