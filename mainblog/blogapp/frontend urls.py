from django.urls import path
from . import views

urlpatterns = [
    # ================= HTML PAGES =================
    path('register-page/', views.register_page, name='register-page'),
    path('login-page/', views.login_page, name='login-page'),
    path('home/', views.home_page, name='home'),
 
]
