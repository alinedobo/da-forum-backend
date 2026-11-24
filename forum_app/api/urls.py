from django.urls import path
from .views import PostCreateListView, PostDetailView, CommentCreateListView, CommentDetailView

urlpatterns = [
    path('posts/', PostCreateListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/comments/', CommentCreateListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', PostDetailView.as_view(), name='comment-detail'),
]