from django.urls import path, include
from testsuits import views
from rest_framework import routers

# 创建路由对象
router = routers.SimpleRouter()
# router = routers.DefaultRouter()
# 注册路由
# prefix为路由前缀，一般添加为应用名即可
# viewset为视图集
router.register(r'testsuits', views.TestsuitsViewSet)

urlpatterns = [

]

urlpatterns += router.urls
