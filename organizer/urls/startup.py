from django.urls import path, re_path

from ..feeds import (
    AtomStartupFeed, Rss2StartupFeed)

from ..views import(
	 NewsLinkCreate, NewsLinkDelete,
    NewsLinkUpdate, StartupCreate, StartupDelete,
    StartupDetail, StartupList, StartupUpdate)

urlpatterns = [
	path('',
		StartupList.as_view(),
		name='organizer_startup_list'),
	path('create/',
		StartupCreate.as_view(),
		name='organizer_startup_create'),
	re_path('(?P<slug>[\w-]+)/',
		StartupDetail.as_view(),
		name='organizer_startup_detail'),
	re_path('(?P<slug>[\w-]+)/update/',
		StartupUpdate.as_view(),
		name='organizer_startup_update'),
	re_path('(?P<slug>[\w-]+)/delete/',
		StartupDelete.as_view(),
		name='organizer_startup_delete'),
	re_path('(?P<startup_slug>[\w\-]+)/add_article_link/',
		NewsLinkCreate.as_view(),
		name='organizer_newslink_create'),
	re_path('(?P<startup_slug>[\w-]+)/(?P<newslink_slug>[\w-]+)/update/',
		NewsLinkUpdate.as_view(),
		name='organizer_newslink_update'),
	re_path('(?P<startup_slug>[\w-]+)/(?P<newslink_slug>[\w-]+)/delete/',
		NewsLinkDelete.as_view(),
		name='organizer_newslink_delete'),
    re_path('(?P<startup_slug>[\w-]+)/atom/',
        AtomStartupFeed(),
        name='organizer_startup_atom_feed'),
    re_path('(?P<startup_slug>[\w-]+)/rss/',
        Rss2StartupFeed(),
        name='organizer_startup_rss_feed'),
   
]