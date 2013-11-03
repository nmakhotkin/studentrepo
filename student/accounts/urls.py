from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns(
    '',
    url(r'^profile/$', 'student.accounts.views.profile'),
    url(r'^login/$', 'student.accounts.views.login'),
    url(r'^registration/$', 'student.accounts.views.registration'),
    # url(r'^logout/$', logout),
)
