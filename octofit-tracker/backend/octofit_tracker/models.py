from django.db import models
from djongo import models as djongo_models


class User(djongo_models.Model):
    """User model for OctoFit Tracker"""
    _id = djongo_models.ObjectIdField()
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
        
    def __str__(self):
        return self.name


class Team(djongo_models.Model):
    """Team model for OctoFit Tracker"""
    _id = djongo_models.ObjectIdField()
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'teams'
        
    def __str__(self):
        return self.name


class Activity(djongo_models.Model):
    """Activity model for OctoFit Tracker"""
    _id = djongo_models.ObjectIdField()
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in minutes")
    calories = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'activities'
        
    def __str__(self):
        return f"{self.user_email} - {self.activity_type}"


class Leaderboard(djongo_models.Model):
    """Leaderboard model for OctoFit Tracker"""
    _id = djongo_models.ObjectIdField()
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    total_points = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard'
        ordering = ['-total_points']
        
    def __str__(self):
        return f"{self.user_email} - {self.total_points} points"


class Workout(djongo_models.Model):
    """Workout model for OctoFit Tracker"""
    _id = djongo_models.ObjectIdField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    duration = models.IntegerField(help_text="Duration in minutes")
    target_muscles = models.CharField(max_length=500)
    
    class Meta:
        db_table = 'workouts'
        
    def __str__(self):
        return self.name
