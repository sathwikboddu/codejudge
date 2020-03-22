from django.conf.urls import url, include
from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('leads/', views.leads, name='leads'),
    path('mark_lead/', views.mark_lead, name='mark_lead'),
    # path('update/', views.update, name='update'),
    # path('delete/', views.delete, name='delete'),
    # path('mark/', views.mark, name='mark'),
]
