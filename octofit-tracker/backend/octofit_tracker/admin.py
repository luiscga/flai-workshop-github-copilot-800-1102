from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin interface for User model"""
    list_display = ['name', 'email', 'team', 'created_at']
    search_fields = ['name', 'email', 'team']
    list_filter = ['team', 'created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin interface for Team model"""
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin interface for Activity model"""
    list_display = ['user_email', 'activity_type', 'duration', 'calories', 'date']
    search_fields = ['user_email', 'activity_type']
    list_filter = ['activity_type', 'date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin interface for Leaderboard model"""
    list_display = ['user_email', 'team', 'total_points', 'rank', 'updated_at']
    search_fields = ['user_email', 'team']
    list_filter = ['team', 'updated_at']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin interface for Workout model"""
    list_display = ['name', 'difficulty', 'duration', 'target_muscles']
    search_fields = ['name', 'description', 'target_muscles']
    list_filter = ['difficulty']
