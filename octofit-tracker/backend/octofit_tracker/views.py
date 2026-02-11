from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)
import os


@api_view(['GET'])
def api_root(request, format=None):
    """API root endpoint that lists all available endpoints"""
    # Use environment variable for codespace URL
    codespace_name = os.environ.get('CODESPACE_NAME', '')
    if codespace_name:
        base_url = f'https://{codespace_name}-8000.app.github.dev/api'
    else:
        # Fallback to relative URLs for local development
        base_url = request.build_absolute_uri('/api')
    
    return Response({
        'users': f'{base_url}/users/',
        'teams': f'{base_url}/teams/',
        'activities': f'{base_url}/activities/',
        'leaderboard': f'{base_url}/leaderboard/',
        'workouts': f'{base_url}/workouts/',
    })


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for User model"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """ViewSet for Team model"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """ViewSet for Activity model"""
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    """ViewSet for Leaderboard model"""
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """ViewSet for Workout model"""
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
