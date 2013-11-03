from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    '',
    url(r'^profile/$', 'student.accounts.views.profile')
)
