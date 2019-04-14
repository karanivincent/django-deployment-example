from django.urls import path
from django.conf.urls import url
from basic_app import views

##TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('other/', views.other, name='other'),
    path('trybootstrap', views.bootstrap, name='bootstrap')
]
