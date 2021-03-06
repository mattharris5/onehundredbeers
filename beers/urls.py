"""URL definition for the beer site"""


from django.conf.urls import url, include
from beers.views import user, validation, contest
import beers.api.views as api_views

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
    url(r'^contests/(?P<contest_id>[0-9]+)/unvalidated_checkins$',
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
        name='contest-player'),
    url(r'^contests/(?P<contest_id>[0-9]+)/players/$',
        contest.contest_players,
        name='contest-players'),
    url(r'^contests/(?P<contest_id>[0-9]+)/beers/(?P<beer_id>[0-9]+)$',
        contest.contest_beer,
        name='contest-beer'),
    url(r'^contests/(?P<contest_id>[0-9]+)/beers/$',
        contest.contest_beers,
        name='contest-beers'),
    url(r'^contests/(?P<contest_id>[0-9]+)/breweries/$',
        contest.contest_breweries,
        name='contest-breweries'),
    url(r'^contests/(?P<contest_id>[0-9]+)/breweries/(?P<brewery_id>[0-9]+)$',
        contest.contest_brewery,
        name='contest-brewery'),
    url(r'^contests/(?P<contest_id>[0-9]+)/challenges/(?P<beer_id>[0-9]+)$',
        contest.contest_challenge,
        name='contest-challenge'),
    url(r'^contests/(?P<contest_id>[0-9]+)/challenges/$',
        contest.contest_challenges,
        name='contest-challenges'),
    url(r'^contests/(?P<contest_id>[0-9]+)/bonuses/$',
        contest.contest_bonuses,
        name='contest-bonuses'),
    url(r'^contests/(?P<contest_id>[0-9]+)/bonuses/(?P<bonus_tag>[A-Za-z0-9]+)$',
        contest.contest_bonus,
        name='contest-bonus'),
    url(r'^contests/(?P<contest_id>[0-9]+)/recover$',
        validation.initiate_recover,
        name='initiate-recover'),
    url(r'^instructions$', contest.instructions, name='instructions'),
    url(r'^api/players/$', 
        api_views.PlayerList.as_view(), 
        name='player-list',),
    url(r'^api/players/(?P<user__username>[A-Za-z0-9_]+)$', 
        api_views.PlayerDetail.as_view(), 
        name='player-detail',),
    url(r'^api/contests/$', 
        api_views.ContestList.as_view(),
        name='contest-list',),
    url(r'^api/contests/(?P<id>[0-9]+)$', 
        api_views.ContestDetail.as_view(),
        name='contest-detail',),
    url(r'^api/contests/(?P<contest_id>[0-9]+)/players/$',
        api_views.ContestPlayerList.as_view(),
        name='contest-player-list',),
    url(r'^api/contests/(?P<contest_id>[0-9]+)/players/(?P<username>[A-Za-z0-9_]+)$',
        api_views.ContestPlayerDetail.as_view(),
        name='contest-player-detail',),
    url(r'^api/contests/(?P<contest_id>[0-9]+)/beers/$',
        api_views.ContestBeerList.as_view(),
        name='contest-beer-list',),
    url(r'^api/contests/(?P<contest_id>[0-9]+)/beers/(?P<contest_beer_id>[0-9]+)$',
        api_views.ContestBeerDetail.as_view(),
        name='contest-beer-detail',),
    url(r'^api/contests/(?P<contest_id>[0-9]+)/breweries/$',
        api_views.ContestBreweryList.as_view(),
        name='contest-brewery-list',),
    url(r'^api/contests/(?P<contest_id>[0-9]+)/breweries/(?P<contest_brewery_id>[0-9]+)$',
        api_views.ContestBreweryDetail.as_view(),
        name='contest-brewery-detail',),
    url(r'^api/contests/(?P<contest_id>[0-9]+)/bonuses/$',
        api_views.ContestBonusList.as_view(),
        name='contest-bonus-list',),
    url(r'^api/contests/(?P<contest_id>[0-9]+)/bonuses/(?P<contest_bonus_id>[0-9]+)$',
        api_views.ContestBonusDetail.as_view(),
        name='contest-bonus-detail',),
    url(r'^api/contests/(?P<contest_id>[0-9]+)/unvalidated_checkins$',
        api_views.UnvalidatedCheckinList.as_view(),
        name='unvalidated-checkin-list',),
    url(r'^api/unvalidated_checkins/(?P<id>[0-9]+)$',
        api_views.UnvalidatedCheckinDetail.as_view(),
        name='unvalidated-checkin-detail',),
    url(r'^api/lookup/beer', api_views.BeerLookup.as_view(), name='beer-lookup'),
    url(r'^api/lookup/brewery', 
        api_views.BreweryLookup.as_view(), 
        name='brewery-lookup'),
]

