from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='run', distance=5)
        Activity.objects.create(user=batman, type='cycle', distance=10)

        # Create workouts
        Workout.objects.create(user=captain, description='Pushups', reps=50)
        Workout.objects.create(user=superman, description='Squats', reps=100)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
