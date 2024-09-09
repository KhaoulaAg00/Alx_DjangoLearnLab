from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,  add_comment, edit_comment, delete_comment, CommentCreateView, CommentUpdateView, CommentDeleteView


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_id>/comments/new/', add_comment, name='add-comment'),
    path('comment/<int:comment_id>/edit/', edit_comment, name='edit-comment'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete-comment'),path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),  # Ensure this pattern exists
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
