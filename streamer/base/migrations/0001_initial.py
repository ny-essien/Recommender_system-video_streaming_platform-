# Generated by Django 5.1.7 on 2025-03-12 09:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="categories/")),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile_pictures/"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("thumbnail", models.ImageField(upload_to="thumbnails/")),
                (
                    "video_file",
                    models.FileField(blank=True, null=True, upload_to="videos/"),
                ),
                ("video_url", models.URLField(blank=True, null=True)),
                ("release_year", models.IntegerField()),
                (
                    "content_type",
                    models.CharField(
                        choices=[("movie", "Movie"), ("tvshow", "TV Show")],
                        max_length=10,
                    ),
                ),
                ("is_trending", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "categories",
                    models.ManyToManyField(related_name="videos", to="base.category"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lists",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "videos",
                    models.ManyToManyField(related_name="in_lists", to="base.video"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Episode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("episode_number", models.IntegerField()),
                ("season_number", models.IntegerField()),
                ("thumbnail", models.ImageField(upload_to="episode_thumbnails/")),
                (
                    "video_file",
                    models.FileField(
                        blank=True, null=True, upload_to="episode_videos/"
                    ),
                ),
                ("video_url", models.URLField(blank=True, null=True)),
                ("duration", models.IntegerField(help_text="Duration in seconds")),
                (
                    "video",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="episodes",
                        to="base.video",
                    ),
                ),
            ],
            options={
                "ordering": ["season_number", "episode_number"],
            },
        ),
        migrations.CreateModel(
            name="WatchHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "progress",
                    models.FloatField(
                        default=0, help_text="Progress percentage (0-100)"
                    ),
                ),
                ("last_watched", models.DateTimeField(auto_now=True)),
                (
                    "episode",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.episode",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="watch_history",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "video",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.video",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Watch History",
                "ordering": ["-last_watched"],
            },
        ),
    ]
