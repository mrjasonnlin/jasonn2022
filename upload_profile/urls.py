from django.urls import path
from . import views

app_name = 'upload_profile'
urlpatterns = [
    path('', views.upload_profile, name='upload_profile'),
    path('add/', views.add, name='add'),
    path('detail/', views.detail, name='detail'),

]
