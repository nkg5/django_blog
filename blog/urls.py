from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('tag/<str:tag>', views.TagPostListView.as_view(), name='tag'),
    path('search/', views.SearchPostListView.as_view(), name='search'),
    path('post/new', views.NewPostView.as_view(), name='post_new'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_view'),
    path('post/<int:pk>/edit', views.EditPostView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', views.DeletePostView.as_view(), name='post_delete'),
    path('post/<int:post_pk>/comment', views.create_comment, name='post_comment_new'),
    path('post/<int:post_pk>/comment/<int:comment_pk>/reply', views.comment_reply, name='post_comment_reply'),
    path('post/<int:post_pk>/comment/<int:comment_pk>/delete', views.comment_delete, name="post_comment_delete")

]
