from django.contrib import admin
from .models import Category, Video, Episode, UserProfile, WatchHistory, UserList

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'release_year', 'is_trending')
    list_filter = ('content_type', 'is_trending', 'categories')
    search_fields = ('title', 'description')
    filter_horizontal = ('categories',)

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'video', 'season_number', 'episode_number')
    list_filter = ('video', 'season_number')
    search_fields = ('title', 'video__title')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__email')

@admin.register(WatchHistory)
class WatchHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_content_title', 'progress', 'last_watched')
    list_filter = ('user', 'last_watched')
    search_fields = ('user__username', 'video__title', 'episode__title')
    
    def get_content_title(self, obj):
        return obj.episode.title if obj.episode else obj.video.title
    get_content_title.short_description = 'Content'

@admin.register(UserList)
class UserListAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_video_count')
    search_fields = ('user__username',)
    filter_horizontal = ('videos',)
    
    def get_video_count(self, obj):
        return obj.videos.count()
    get_video_count.short_description = 'Videos'