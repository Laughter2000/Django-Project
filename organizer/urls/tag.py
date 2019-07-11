from django.urls import path, re_path

from ..views import (
	TagCreate, TagDelete, TagUpdate, TagDetail, 
	TagList)


urlpatterns = [
    path('',
		TagList.as_view(),
		name='organizer_tag_list'),
	path('create/',
		TagCreate.as_view(),
		name='organizer_tag_create'),
    re_path('(?P<slug>[\w-]+)/',
		TagDetail.as_view(),
		name='organizer_tag_detail'),
	re_path('(?P<slug>[\w-]+)/update/',
		TagUpdate.as_view,
		name='organizer_tag_update'),
	re_path('(?P<slug>[\w-]+)/delete/',
		TagDelete.as_view,
		name='organizer_tag_delete'),
  
]
