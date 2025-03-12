from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Video(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('movie', 'Movie'),
        ('tvshow', 'TV Show'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    release_year = models.IntegerField()
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES)
    categories = models.ManyToManyField(Category, related_name='videos')
    is_trending = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Episode(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='episodes')
    title = models.CharField(max_length=200)
    episode_number = models.IntegerField()
    season_number = models.IntegerField()
    thumbnail = models.ImageField(upload_to='episode_thumbnails/')
    video_file = models.FileField(upload_to='episode_videos/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    duration = models.IntegerField(help_text="Duration in seconds")
    
    def __str__(self):
        return f"{self.video.title} - S{self.season_number}:E{self.episode_number} - {self.title}"
    
    class Meta:
        ordering = ['season_number', 'episode_number']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    def __str__(self):
        return self.user.username

class WatchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watch_history')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, null=True, blank=True)
    progress = models.FloatField(default=0, help_text="Progress percentage (0-100)")
    last_watched = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        content = self.episode if self.episode else self.video
        return f"{self.user.username} - {content}"
    
    class Meta:
        verbose_name_plural = "Watch History"
        ordering = ['-last_watched']

class UserList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists')
    videos = models.ManyToManyField(Video, related_name='in_lists')
    
    def __str__(self):
        return f"{self.user.username}'s List"