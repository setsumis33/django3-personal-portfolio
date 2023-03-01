
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.all_blog, name='all_blogs'), # для создания ссылки в браузере
    path('<int:blog_id>/', views.detail, name='detail'), #для нумерации блогов в ссылке
]
