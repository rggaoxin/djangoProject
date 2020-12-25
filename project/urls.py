from django.urls import path
from project import views

urlpatterns = [
    path('index/', views.index),
    path('indexview/', views.IndexView.as_view()),
    # path('indexview/<int:pk>/', views.IndexView.as_view()),  # int为路径参数类型转化器，：左边为转换器，右边为参数别名，int、slog、uuid
    path('projects/', views.ProjectsList.as_view()),
    path('projects/<int:pk>/', views.ProjectsDetail.as_view()),
]
