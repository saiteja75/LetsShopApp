from django.urls import path, include
from UserAuth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="Index"),
    path('login', views.login, name='Login'),
    path('signup', views.signup, name='Signup'),
    path('forgot', views.forgot, name='Forgot'),
    path('logout', views.logout, name='Logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='forgot.html')),
    path('password_reset_sent/',auth_views.PasswordChangeDoneView.as_view()),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view()),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view())

]
