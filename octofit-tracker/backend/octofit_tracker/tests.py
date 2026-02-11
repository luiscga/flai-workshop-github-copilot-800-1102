from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTestCase(TestCase):
    """Test case for User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            team="Test Team"
        )
    
    def test_user_creation(self):
        """Test user is created correctly"""
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(str(self.user), "Test User")


class TeamModelTestCase(TestCase):
    """Test case for Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team"
        )
    
    def test_team_creation(self):
        """Test team is created correctly"""
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(str(self.team), "Test Team")


class ActivityModelTestCase(TestCase):
    """Test case for Activity model"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_email="test@example.com",
            activity_type="Running",
            duration=30,
            calories=250
        )
    
    def test_activity_creation(self):
        """Test activity is created correctly"""
        self.assertEqual(self.activity.user_email, "test@example.com")
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)


class LeaderboardModelTestCase(TestCase):
    """Test case for Leaderboard model"""
    
    def setUp(self):
        self.leaderboard = Leaderboard.objects.create(
            user_email="test@example.com",
            team="Test Team",
            total_points=100,
            rank=1
        )
    
    def test_leaderboard_creation(self):
        """Test leaderboard entry is created correctly"""
        self.assertEqual(self.leaderboard.user_email, "test@example.com")
        self.assertEqual(self.leaderboard.total_points, 100)


class WorkoutModelTestCase(TestCase):
    """Test case for Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            name="Push-ups",
            description="Upper body exercise",
            difficulty="Medium",
            duration=15,
            target_muscles="Chest, Arms"
        )
    
    def test_workout_creation(self):
        """Test workout is created correctly"""
        self.assertEqual(self.workout.name, "Push-ups")
        self.assertEqual(self.workout.difficulty, "Medium")


class APITestCase(APITestCase):
    """Test case for API endpoints"""
    
    def test_api_root(self):
        """Test API root endpoint"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
