from urllib import request
from xml.etree.ElementTree import Comment

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tweet
from users.models import User

@login_required
def feed(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        tweet_id = request.POST.get('tweet_id')
        
        if tweet_id:
            tweet = Tweet.objects.get(id=tweet_id)
            Comment.objects.create(user=request.user, tweet=tweet, content=content)
        elif content:
            Tweet.objects.create(user=request.user, content=content)
        return redirect('posts:feed')

    user_and_following = list(request.user.following.all()) + [request.user]
    tweets = Tweet.objects.filter(user__in=user_and_following)
    
    return render(request, 'posts/feed.html', {'tweets': tweets})

@login_required
def follow_user(request, username):
    user_to_follow = User.objects.get(username=username)
    if user_to_follow != request.user:
        if user_to_follow in request.user.following.all():
            request.user.following.remove(user_to_follow)
        else:
            request.user.following.add(user_to_follow)
    return redirect('posts:feed')

@login_required
def like_tweet(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    if request.user in tweet.likes.all():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)
    return redirect('posts:feed')