from django.urls import path, re_path

from .views import  (
	PostArchiveMonth, PostArchiveYear, PostCreate,
    PostDelete, PostList, PostUpdate, PostDetail)

urlpatterns = [
    path('',
        PostList.as_view(),
        name='blog_post_list'),
    re_path('create/',
        PostCreate.as_view(),
        name='blog_post_create'),
    re_path('(?P<year>\d{4})/',
        PostArchiveYear.as_view(),
        name='blog_post_archive_year'),
    re_path('(?P<year>\d{4})/(?P<month>\d{1,2})/',
        PostArchiveMonth.as_view(),
        name='blog_post_archive_month'),
    re_path('(?P<month>\d{1,2})/(?P<slug>[\w-]+)/',
        PostDetail.as_view(),
        name='blog_post_detail'),
    re_path('(?P<slug>[\w-]+)/delete/',
        PostDelete.as_view(),
        name='blog_post_delete'),
    re_path('(?P<slug>[\w-]+)/update/',
        PostUpdate.as_view(),
        name='blog_post_update'),
]