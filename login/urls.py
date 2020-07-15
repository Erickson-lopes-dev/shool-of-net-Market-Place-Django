from django.conf.urls import url

from . import views

urlpatterns = [
    url('register/', views.register, name='login_register'),
    url('register/sucess', views.register_sucess, name='login_register_sucess')
]