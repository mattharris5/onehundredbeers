from django.test import TestCase, TransactionTestCase, override_settings
from django.test import Client
from django.contrib.auth.models import User, Group, Permission
from django.core.urlresolvers import reverse
from beers.models import Contest, Player, Contest_Player, Unvalidated_Checkin, Contest_Checkin
from django.utils import timezone
import datetime
import json

@override_settings(SECURE_SSL_REDIRECT=False, ROOTURL_CONF='beers.urls')
class ContestTestCase(TestCase):

    fixtures = [ 'permissions', 'contest_tests']

    def setUp(self):
        # Relies on the fixture with users, players, and contest players
        # with the same primary keys, with pk=4 being the contest runner
        Unvalidated_Checkin.objects.create_checkin(
            contest_player=Contest_Player.objects.get(user_name='user1'),
            untappd_title='Title 1',
            brewery='Unknown Brewery',
            beer='Unknown Beer',
            untappd_checkin='https://example.com/checkin/checkin1',
            untappd_checkin_date=timezone.make_aware(datetime.datetime(2016, 5, 1)),
        )
        # This should match the beer with pk=1 and point value of 1
        Unvalidated_Checkin.objects.create_checkin(
            contest_player=Contest_Player.objects.get(user_name='user1'),
            untappd_title='Title 2',
            brewery='Brewery 2',
            beer='Beer 2',
            untappd_checkin='https://example.com/checkin/checkin2',
            untappd_checkin_date=timezone.make_aware(datetime.datetime(2016, 5, 1)),
        )
        # This shouldm atch the beer with pk=3 and point value of 3
        Unvalidated_Checkin.objects.create_checkin(
            contest_player=Contest_Player.objects.get(user_name='user1'),
            untappd_title='Title 3',
            brewery='Brewery 3',
            beer='Beer 3',
            untappd_checkin='https://example.com/checkin/checkin3',
            untappd_checkin_date=timezone.make_aware(datetime.datetime(2016, 5, 1)),
        )

    def tearDown(self):
        # Removes all checkin data and resets everyone's point values and beer counts
        Unvalidated_Checkin.objects.all().delete()
        Contest_Checkin.objects.all().delete()
        Contest_Player.objects.all().update(beer_count=0, beer_points=0,
                    last_checkin_date=None, last_checkin_beer=None,
                    last_checkin_load=timezone.make_aware(datetime.datetime(2016, 1, 1)),)

    def test_successful_checkin_validate(self):
        """Logs in as the correct user and validates a beer"""
        c = Client()
        self.assertTrue(c.login(username='runner1', password='password1%'))
        uv = Unvalidated_Checkin.objects.get(untappd_title='Title 2')
        response = c.post(reverse('update-checkin', kwargs={'contest_id': 1, 'uv_checkin': uv.id,}),
                content_type='application/json',
                data=json.dumps({ 'validate-beer': 'Validate', 'contest-beer': 1,}),
                HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, 200)
        q = Contest_Checkin.objects.filter(contest_beer__id=1, contest_player__id=1)
        self.assertEqual(q.count(), 1)
        checkin = q.get()
        self.assertEqual(checkin.checkin_points, 1)
        self.assertEqual(checkin.untappd_checkin, 'https://example.com/checkin/checkin2')
        self.assertEqual(checkin.contest_player.beer_count, 1)
        self.assertEqual(checkin.contest_player.beer_points, 1)
        self.assertEqual(Unvalidated_Checkin.objects.filter(untappd_title='Title 2').count(), 0)

    def test_invalid_checkin_validate(self):
        """Tests what happens when an unvalidated checkin is removed"""
        c = Client()
        self.assertTrue(c.login(username='runner1', password='password1%'))
        uv = Unvalidated_Checkin.objects.get(untappd_title='Title 2')
        response = c.post(reverse('update-checkin', kwargs={'contest_id': 1, 'uv_checkin': uv.id,}),
                content_type='application/json',
                data=json.dumps({ 'remove-beer': 'Remove',}),
                HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, 200)
        contest_player = Contest_Player.objects.get(id=1)
        self.assertEqual(contest_player.beer_count, 0)
        self.assertEqual(contest_player.beer_points, 0)
        self.assertEqual(Unvalidated_Checkin.objects.filter(untappd_title='Title 2').count(), 0)
