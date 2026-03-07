# from django.urls import path
# from . import views

# urlpatterns = [

#     # ================= FRONTEND PAGES =================
    
#     path('register-page/', views.RegisterView.as_view(), name='register-page'),
#     path('login-page/', views.LoginView.as_view(), name='login-page'),
#     path('home/', views.home_page, name='home'),

#     # ================= API POSTS =================
#     path('api/posts/', views.PostListCreateView.as_view(), name='post-list-create'),
#     path('api/posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
#     path('api/posts/<int:pk>/like/', views.toggle_like, name='toggle-like'),

#     # ================= API COMMENTS =================
#     path('api/comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
#     path('api/comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),

#     # ================= API PROFILE =================
#     path('api/profile/', views.MyProfileView.as_view(), name='my-profile'),

#     # ================= API MY LATEST POST =================
#     path('api/my-latest-post/', views.MyLatestPostView.as_view(), name='my-latest-post'),
# ]














from django.urls import path
from .views import (
    register_page,
    login_page,
    logout_view,
    home_page,
    PostView,
    PostDetailView,
    ToggleLikeView,
    CommentView,
    MyProfileView,
)

urlpatterns = [

    # ================= TEMPLATE ROUTES =================
    path('', home_page, name='home'),
    path('register-page/', register_page, name='register'),
    path('login-view/', login_page, name='login'),
    path('logout/', logout_view, name='logout'),

    # ================= API ROUTES =================
    path('api/posts/', PostView.as_view(), name='posts'),
    path('api/posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('api/posts/<int:pk>/like/', ToggleLikeView.as_view(), name='toggle_like'),
    path('api/posts/<int:post_id>/comments/', CommentView.as_view(), name='comments'),
    path('api/profile-page/', MyProfileView.as_view(), name='profile'),
]
