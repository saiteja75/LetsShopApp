from django.urls import path, include
from UserAuth import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('login', views.login, name='Login'),
    path('signup', views.signup, name='Signup'),
    path('forgot', views.forgot, name='Forgot')
]
