"""iashop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap
# from photologue.sitemaps import GallerySitemap, PhotoSitemap
from . import common
#
# sitemaps = {
#             'photologue_galleries': GallerySitemap,
#             'photologue_photos': PhotoSitemap,
#             }
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
     url(r'^chaining/', include('smart_selects.urls')),
    url(r'', include('auction.urls', namespace='auctions')),
    url(r'', include('account.urls', namespace='accounts')),
    url(r'', include('cart.urls', namespace='shopping-cart')),
    url(r'', include('pages.urls', namespace='pages')),
    url(r'^', include('django.contrib.auth.urls')),
    url('^inbox/notifications/', include('notifications.urls', namespace='notifications')),
    # url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    # name='django.contrib.sitemaps.views.sitemap'),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^grapelli/', include('grappelli.urls')),


#     ratings app
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),

]
# + static(common.STATIC_URL, document_root=common.STATIC_ROOT)
# urlpatterns += staticfiles_urlpatterns()

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if common.DEBUG:
    urlpatterns += static(common.MEDIA_URL,
    document_root=common.MEDIA_ROOT)


# from django.conf.urls import handler400, handler403, handler404, handler500

handler404 = 'pages.views.not_found'
handler500 = 'pages.views.server_error'
handler403 = 'pages.views.permission_denied'
handler400 = 'pages.views.bad_request'