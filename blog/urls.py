from django.urls import path
from .views import (
    PostListView, PostDetail, PostNew, PostUpdate, PostDelete
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/full', PostDetail.as_view(), name='post_full_detail'),
    path('post/new/', PostNew.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
