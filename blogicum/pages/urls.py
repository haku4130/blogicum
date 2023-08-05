from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail')
]
