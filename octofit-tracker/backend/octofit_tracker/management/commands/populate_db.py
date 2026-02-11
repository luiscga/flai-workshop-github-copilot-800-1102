from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database population...')
        
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League of America'
        )
        
        # Create Users (superheroes)
        self.stdout.write('Creating users...')
        marvel_heroes = [
            {'name': 'Iron Man', 'email': 'tony.stark@marvel.com'},
            {'name': 'Captain America', 'email': 'steve.rogers@marvel.com'},
            {'name': 'Thor', 'email': 'thor.odinson@marvel.com'},
            {'name': 'Black Widow', 'email': 'natasha.romanoff@marvel.com'},
            {'name': 'Hulk', 'email': 'bruce.banner@marvel.com'},
            {'name': 'Spider-Man', 'email': 'peter.parker@marvel.com'},
        ]
        
        dc_heroes = [
            {'name': 'Superman', 'email': 'clark.kent@dc.com'},
            {'name': 'Batman', 'email': 'bruce.wayne@dc.com'},
            {'name': 'Wonder Woman', 'email': 'diana.prince@dc.com'},
            {'name': 'The Flash', 'email': 'barry.allen@dc.com'},
            {'name': 'Aquaman', 'email': 'arthur.curry@dc.com'},
            {'name': 'Green Lantern', 'email': 'hal.jordan@dc.com'},
        ]
        
        marvel_users = []
        for hero in marvel_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team='Team Marvel'
            )
            marvel_users.append(user)
        
        dc_users = []
        for hero in dc_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team='Team DC'
            )
            dc_users.append(user)
        
        all_users = marvel_users + dc_users
        
        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = [
            'Running', 'Swimming', 'Cycling', 'Weight Training',
            'Yoga', 'Boxing', 'HIIT', 'CrossFit'
        ]
        
        for user in all_users:
            # Create 3-5 activities per user
            num_activities = random.randint(3, 5)
            for i in range(num_activities):
                days_ago = random.randint(0, 30)
                activity_date = datetime.now() - timedelta(days=days_ago)
                
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 90)
                calories = duration * random.randint(8, 15)
                
                Activity.objects.create(
                    user_email=user.email,
                    activity_type=activity_type,
                    duration=duration,
                    calories=calories
                )
        
        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        for user in all_users:
            # Calculate total points from activities
            user_activities = Activity.objects.filter(user_email=user.email)
            total_points = sum(activity.calories for activity in user_activities)
            
            Leaderboard.objects.create(
                user_email=user.email,
                team=user.team,
                total_points=total_points,
                rank=0  # Will be updated below
            )
        
        # Update ranks based on points
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_points')
        for idx, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = idx
            entry.save()
        
        # Create Workouts
        self.stdout.write('Creating workouts...')
        workouts = [
            {
                'name': 'Super Soldier Strength Training',
                'description': 'Captain America\'s intensive strength building routine focusing on functional fitness',
                'difficulty': 'Hard',
                'duration': 60,
                'target_muscles': 'Full body, Core, Legs'
            },
            {
                'name': 'Asgardian Warrior Workout',
                'description': 'Thor\'s legendary training regimen combining power and endurance',
                'difficulty': 'Extreme',
                'duration': 75,
                'target_muscles': 'Chest, Back, Shoulders, Arms'
            },
            {
                'name': 'Speedster Sprint Circuit',
                'description': 'The Flash\'s high-intensity cardio and speed training program',
                'difficulty': 'Medium',
                'duration': 45,
                'target_muscles': 'Legs, Cardio, Core'
            },
            {
                'name': 'Amazonian Combat Training',
                'description': 'Wonder Woman\'s warrior training focusing on combat readiness',
                'difficulty': 'Hard',
                'duration': 60,
                'target_muscles': 'Full body, Core, Arms'
            },
            {
                'name': 'Web-Slinger Agility',
                'description': 'Spider-Man\'s agility and flexibility focused workout',
                'difficulty': 'Medium',
                'duration': 40,
                'target_muscles': 'Core, Flexibility, Balance'
            },
            {
                'name': 'Dark Knight Conditioning',
                'description': 'Batman\'s comprehensive conditioning program for peak performance',
                'difficulty': 'Hard',
                'duration': 70,
                'target_muscles': 'Full body, Core, Cardio'
            },
            {
                'name': 'Atlantean Aqua Fitness',
                'description': 'Aquaman\'s water-based endurance and strength training',
                'difficulty': 'Medium',
                'duration': 50,
                'target_muscles': 'Shoulders, Back, Core'
            },
            {
                'name': 'Arc Reactor Energy Blast',
                'description': 'Iron Man\'s high-tech HIIT workout for maximum calorie burn',
                'difficulty': 'Hard',
                'duration': 35,
                'target_muscles': 'Full body, Cardio'
            },
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)
        
        # Print summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(f'Teams created: {Team.objects.count()}')
        self.stdout.write(f'Users created: {User.objects.count()}')
        self.stdout.write(f'Activities created: {Activity.objects.count()}')
        self.stdout.write(f'Leaderboard entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'Workouts created: {Workout.objects.count()}')
        self.stdout.write(self.style.SUCCESS('\nDatabase successfully populated with superhero test data!'))
