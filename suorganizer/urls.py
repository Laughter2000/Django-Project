"""suorganizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from blog import urls as blog_urls
from blog.views import PostList
from contact import urls as contact_urls
from organizer.urls import(
    startup as startup_urls, tag as tag_urls)
from django.views.generic import (
    RedirectView, TemplateView)
from user import urls as user_urls
from blog.feeds import AtomPostFeed, Rss2PostFeed
admin.site.site_header = 'Startup Organizer Admin'
admin.site.site_title = 'Startup Organizer Site Admin'

sitenews = [
    path('atom/',
        AtomPostFeed(),
        name='blog_atom_feed'),
    path('rss/',
        Rss2PostFeed(),
        name='blog_rss_feed'),
]

urlpatterns = [
	path ('', RedirectView.as_view(
                    pattern_name='blog_post_list',
                    permanent=False)),
     path('about/',
        TemplateView.as_view(
            template_name='site/about.html'),
        name='about_site'),
    path('admin/', admin.site.urls),
    path('blog/', include(blog_urls)),
    path('contact/', include(contact_urls)),
    path('startup/', include(startup_urls)),
    path('tag/', include(tag_urls)),
    path('user/',include(user_urls, namespace='dj-auth')), 
    path('sitenews/', include(sitenews)),   
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]