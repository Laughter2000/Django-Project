from django.urls import path, re_path

from ..views import (
	NewsLinkCreate, NewsLinkDelete,
    NewsLinkUpdate)



urlpatterns = [
	path('create/',
		NewsLinkCreate.as_view(),
		name='organizer_newslink_create'),
	re_path('update/(?P<pk>\d+)/',
		NewsLinkUpdate.as_view(),
		name='organizer_newslink_update'),
	re_path('delete/(?P<pk>\d+)/',
		NewsLinkDelete.as_view(),
		name='organizer_newslink_delete'),

]