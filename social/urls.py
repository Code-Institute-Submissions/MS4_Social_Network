from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView, CommentEditView, ProfileView, ProfileEditView, AddFollower, RemoveFollower, AddLike, Dislike, UserSearch, ListFollowers, AddCommentLike, AddCommentDislike, CommentReplyView

urlpatterns = [
    # Post URLS
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLS
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment-like'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike', AddCommentDislike.as_view(), name='comment-dislike'),
    path('post/<int:post_pk>/comment/<int:pk>/reply', CommentReplyView.as_view(), name='comment-reply'),
    path('post/<int:post_pk>/comment/edit/<int:pk>/', CommentEditView.as_view(), name='comment-edit'),

    # Like URLS
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', Dislike.as_view(), name='dislike'),

    # Profile URLS
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),

    # Followers URLS
    path('profile/<int:pk>followers/', ListFollowers.as_view(), name='list-followers'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    path('search/', UserSearch.as_view(), name='profile-search'),
]
