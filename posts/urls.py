from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.feed, name='feed'),
    path('follow/<str:username>/', views.follow_user, name='follow'),
    path('like/<int:tweet_id>/', views.like_tweet, name='like'),
]