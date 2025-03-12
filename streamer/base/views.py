from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Video, Category, WatchHistory, UserList
from django.contrib.auth import login, authenticate, logout

def home(request):
    # Get trending movies/shows
    trending_videos = Video.objects.filter(is_trending=True)[:10]
    
    # Get categories
    categories = Category.objects.all()[:4]
    
    # Get continue watching for authenticated users
    continue_watching = []
    if request.user.is_authenticated:
        watch_history = WatchHistory.objects.filter(user=request.user).order_by('-last_watched')[:4]
        continue_watching = [
            {
                'thumbnail': history.episode.thumbnail if history.episode else history.video.thumbnail,
                'title': history.episode.video.title if history.episode else history.video.title,
                'episode_info': f"S{history.episode.season_number}:E{history.episode.episode_number} \"{history.episode.title}\"" if history.episode else "",
                'progress': history.progress
            }
            for history in watch_history
        ]
    
    context = {
        'trending_movies': trending_videos,
        'categories': categories,
        'continue_watching': continue_watching,
    }
    
    return render(request, 'base/index.html', context)

def sign_in(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
    return render(request, 'base/signin.html')


def sign_out(request):

    logout(request)
    return redirect('home')

def register(request):
    return render(request, "base/registration.html")

def reset_password(request):
    return render(request, "base/password_reset.html")

def movies(request):
    movies = Video.objects.filter(content_type='movie')
    return render(request, 'base/movies.html', {'movies': movies})

def tvshows(request):
    tvshows = Video.objects.filter(content_type='tvshow')
    return render(request, 'base/tvshows.html', {'tvshows': tvshows})

@login_required
def mylist(request):
    try:
        user_list = UserList.objects.get(user=request.user)
        videos = user_list.videos.all()
    except UserList.DoesNotExist:
        videos = []
    
    return render(request, 'base/mylist.html', {'videos': videos})

def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    
    # Update watch history for authenticated users
    if request.user.is_authenticated:
        watch_history, created = WatchHistory.objects.get_or_create(
            user=request.user,
            video=video,
            episode=None
        )
        
        # If this is a new view, set progress to 0
        if created:
            watch_history.progress = 0
            watch_history.save()
    
    return render(request, 'base/video_detail.html', {'video': video})

@login_required
def add_to_list(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    user_list, created = UserList.objects.get_or_create(user=request.user)
    
    # Add to list if not already there
    if video not in user_list.videos.all():
        user_list.videos.add(video)
    
    # Redirect back to the previous page
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def remove_from_list(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    try:
        user_list = UserList.objects.get(user=request.user)
        user_list.videos.remove(video)
    except UserList.DoesNotExist:
        pass
    
    # Redirect back to the previous page
    return redirect(request.META.get('HTTP_REFERER', 'home'))