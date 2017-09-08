"""codemancer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import (url, include)
from django.contrib import admin
from rest_framework import routers
from pages.views import (
        snippet_detail, login_page, create_snippet,
        list_snippets, snippet_change,
        about, LanguageViewSet)


router = routers.DefaultRouter()
router.register(r'tags', LanguageViewSet)

# create
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^display/(?P<pk>\d+)', snippet_detail, name='snippet_detail'),
    url(r'^login/', login_page, name='login_page'),
    url(r'^pasting/', create_snippet, name='create_snippet'),
    url(r'^list_snips/', list_snippets, name='list_snippets'),
    url(r'^snippet/change/(?P<pk>\d+)', snippet_change, name='snippet_change'),
    url(r'^about/', about, name='about'),
    url(r'api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
