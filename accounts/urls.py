from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from accounts.views import CustomLoginView

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    # login
    path('logout/', views.logout_view, name='logout'),
    # logout
    path('signup/', views.signup_view, name='signup'),
    # signup
    path('login/', CustomLoginView.as_view(), name='login'),

    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

]
