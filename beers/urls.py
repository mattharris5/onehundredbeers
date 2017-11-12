"""URL definition for the beer site"""


from django.conf.urls import url, include
from beers.views import user, validation, contest


urlpatterns = [
    url(r'^$', contest.index, name='index'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^signup$', user.signup, name='signup'),
    url(r'^profile', user.update_profile, name='profile'),
    url(r'^contests/$', contest.contests, name='contests'),
    url(r'^contests/add$', contest.contest_add, name='contest-add'),
    url(r'^contests/(?P<contest_id>[0-9]+)/$',
        contest.contest,
        name='contest'),
    url(r'^contests/(?P<contest_id>[0-9]+)/join$',
        contest.contest_join,
        name='contest-join'),
    url(r'^contests/(?P<contest_id>[0-9]+)/validate$',
        validation.unvalidated_checkins,
        name='unvalidated-checkins'),
    url(r'^contests/(?P<contest_id>[0-9]+)/validate_api$',
        validation.unvalidated_checkins_json,
        name='unvalidated-checkins-json'),
    url(r'^contests/(?P<contest_id>[0-9]+)/unvalidated_checkins/(?P<uv_checkin>[0-9]+)$',
        validation.delete_checkin,
        name='delete-checkin'),
    url(r'^contests/(?P<contest_id>[0-9]+)/checkins$',
        validation.validate_checkin,
        name='validate-checkin'),
    url(r'^contests/(?P<contest_id>[0-9]+)/players/(?P<username>[^/]+)$',
        contest.contest_player,
        name='player-detail'),
    url(r'^contests/(?P<contest_id>[0-9]+)/beers/(?P<beer_id>[0-9]+)$',
        contest.contest_beer,
        name='beer-detail'),
    url(r'^contests/(?P<contest_id>[0-9]+)/recover$',
        validation.initiate_recover,
        name='initiate-recover'),
    url(r'^instructions$', contest.instructions, name='instructions'),
]
