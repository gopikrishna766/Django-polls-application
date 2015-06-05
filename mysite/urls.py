"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from polls import views, question
import polls

 
urlpatterns = [
    url(r'^polls/', include('mysite.urls', namespace="polls")),
	url(r'^$', 'polls.views.login'),
	url(r'^admin/', include(admin.site.urls)),
    # user auth urls
    url(r'^polls/auth/$', 'polls.views.auth_view'),
    url(r'^polls/logout/$', 'polls.views.logout'),
    url(r'^polls/loggedin/$', 'polls.views.loggedin'),
    url(r'^polls/invalid/$', 'polls.views.invalid_login'),
    url(r'^polls/login/$', 'polls.views.login'),
    url(r'^polls/send_mail/$', 'polls.views.send_mail_info'),
    url(r'^polls/request_mail/$', 'polls.views.request_mail'),
    url(r'^polls/password/reset/$', 'django.contrib.auth.views.password_reset', name ='reset_password_reset1'),
    url(r'^polls/password/reset/done/$', 'django.contrib.auth.views.password_reset_done', name = 'password_reset_done'),
    url(r'^polls/password/reset/(?P<uidb64>[09A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name = 'password_reset_confirm'),
    url(r'^polls/password/done$', 'django.contrib.auth.views.password_reset_complete', name = 'password_reset_complete'),
    url(r'^accounts/login/$', 'polls.views.login'),
    url(r'^polls/index/$', question.IndexView.as_view(), name='index'),
    url(r'^polls/index/(?P<pk>[0-9]+)/$', question.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', question.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
 ]
