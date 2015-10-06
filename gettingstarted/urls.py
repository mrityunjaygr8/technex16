from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^signup/$', hello.views.signup, name='signup'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup_email/$',hello.views.signup_email,name='signup_email'),
    url(r'^login_email/$',hello.views.login_email,name='login_email'),
    url(r'^login/$',hello.views.login,name='login'),
    url(r'^signup2/$',hello.views.signup2,name='signup2'),
    url(r'^signup3/$', hello.views.signup3, name='signup3'),
    url(r'^teamreg/$',hello.views.teamreg, name='teamreg'),
    url(r'^logout/$',hello.views.logout,name='logout'),
    url(r'^team/(?P<team_slug>[\w\-]+)/$',hello.views.team,name='team'),
    url(r'^team/modify/(?P<team_slug>[\w\-]+)/$',hello.views.team_modify,name='team_modify'),
    url(r'^teamdel/(?P<team_slug>[\w\-]+)/$',hello.views.team_delete,name='team_delete'),
    url(r'^google_login/$',hello.views.google_login,name="google_login"),
    url(r'^facebook_login/$',hello.views.facebook_login,name="facebook_login"),
    url(r'^(?P<email_slug>[\w\-]+)/$',hello.views.dashboard,name='dashboard'),
)
