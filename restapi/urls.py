from django.conf.urls import url, include
from django.urls import path, include
from . import views

app_name = 'restapi'

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('insert/', views.insert, name='insert'),
    path('fetch/', views.fetch, name='fetch'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('mark/', views.mark, name='mark'),
]
