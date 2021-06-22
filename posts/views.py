from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
import datetime
from datetime import datetime, timedelta

def update_posts_expiration():
    """
    Function checks if the non-expired posts have passed their expiration_time and 
    if so it changes is_expired attribute from the Post object to True. To be called
    everytime we call a view
    """
    #adds all the objects that are not expired to posts
    posts = Post.objects.filter(is_expired=False)
    #get the actual time
    time_now = timezone.now()
    #loop through all the posts and calculate the expiration date and time
    for post in posts:
        expiry_time = (post.created_at + post.expiration_time)
        #change the is_expired variable to true if the date and time now are after the expiry_time
        if (time_now > expiry_time):
            post.is_expired = True
            post.save()

@api_view(['GET'])
def all_posts_list(request):
    """
    Returns all posts in database
    """
    #update is_expired in all posts
    update_posts_expiration()
    #put all posts into post
    post = Post.objects.all()
    #create serializer with the posts
    serializer = ViewPostSerializer(post, many=True)
    #return serializer view
    return Response(serializer.data)

@api_view(['GET'])
def posts_per_topic_all(request, pk):
    """
    returns all posts per topic
    """
    #update is_expired in all posts
    update_posts_expiration()
    #get all posts with a certain topic
    posts = Post.objects.filter(topic=pk)
    serializer = ViewPostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def expired_posts_list(request):
    """
    Returns expired posts
    """
    update_posts_expiration()
    #get posts that are expired
    post = Post.objects.filter(is_expired=True)
    serializer = ViewPostSerializer(post, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def expired_posts_per_topic_list(request, pk):
    """
    Returns expired posts in a topic
    """
    update_posts_expiration()
    #get posts that are expired in a certain topic
    post = Post.objects.filter(is_expired=True, topic=pk)
    serializer = ViewPostSerializer(post, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def not_expired_post_list(request):
    """
    Returns non-expired posts 
    """
    update_posts_expiration()
    #get posts that are not expired
    filtered_posts = Post.objects.filter(is_expired=False)
    serializer = ViewPostSerializer(filtered_posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def not_expired_posts_per_topic_list(request, pk):
    """
    Returns not expired posts in a topic
    """
    update_posts_expiration()
    #get posts that are not expired in a certain topic
    post = Post.objects.filter(is_expired=False, topic=pk)
    serializer = ViewPostSerializer(post, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def most_active_post(request, pk):
    """
    Returns post with highest number of likes and dislikes per topic
    """
    update_posts_expiration()
    posts = Post.objects.filter(topic=pk)
    highest_likes = 0
    highest_dislikes = 0
    highest_total_count = 0
    new_total_count = 0
    post_id = 0
    for post in posts:

        if (post.likes_count > highest_likes):
            highest_likes = post.likes_count 
            
        if (post.dislikes_count > highest_dislikes):
            highest_dislikes = post.dislikes_count 

        new_total_count = highest_likes + highest_dislikes

        if (new_total_count > highest_total_count):
            post_id = post.id
            highest_total_count = new_total_count

    post = Post.objects.filter(id=post_id)
        
    serializer = ViewPostSerializer(post, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def post_new(request, *args, **kwargs):
    """
    format:
    {
    "title" : "my post",
    "body": "Hello World 4",
    "topic": "Health",
    "expiration_time": "00:02:00"
    }
    Topics available: Tech, Politics, Health or Sports
    """
    #serializes the input from the user
    serializer = PostSerializer(data=request.data)
    #if the serializer has the right format save it to database
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors)



@api_view(['POST'])
def comment_post(request, pk):
    update_posts_expiration()
    """
    format:
    {
    "comment" : "hello"
    }
    
    """
    #gets posts per id
    post = Post.objects.get(id=pk)
    #if the post is not expired post comment serializer to database 
    if post.is_expired == False:
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
            return Response(serializer.data)
        return Response(serializer.errors)
    else: 
        return Response("You can't comment on a expired post")


@api_view(['GET', 'POST'])
def like(request, pk):
    """
    When the request method is POST it increments the likes of
    the post by 1. Can't POST if disliking own post, or if it's expired
    """
    update_posts_expiration()
    post = 0;
    post = Post.objects.get(id=pk)
    #if the post is expired you user can't like it
    if post.is_expired == True:
        return Response("You can't interact with a expired post")
    else:
        #if the post is not expired then increment the likes count by 1 and save a serializer of like to the database with user and post information
        if request.method == "POST":
            if request.user != post.user:
                post.likes_count += 1
                post.save()
                serializer = LikeSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save(user=request.user, liked_post=post)
                    return Response("you liked the post with title: " + post.title)
                else:
                    return Response(serializer.errors)
            else:
                return Response("you can't like your own post")
            

    return Response("you didn't like the post yet")

@api_view(['GET', 'POST'])
def dislike(request, pk):
    """
    When the request method is POST it increments the likes of
    the post by 1. Can't POST if disliking own post, or if it's expired
    """
    update_posts_expiration()
    post = 0;
    post = Post.objects.get(id=pk)
    if post.is_expired == True:
        return Response("You can't interact with a expired post")
    else:
        if request.method == "POST":
            if request.user != post.user:
                post.dislikes_count += 1
                post.save()
                serializer = DislikeSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save(user=request.user, disliked_post=post)
                    return Response("you disliked the post with title: " + post.title)
                else:
                    return Response(serializer.errors)
            else:
                return Response("you can't dislike your own post")
            

    return Response("you didn't dislike the post yet")
    
@api_view(['GET'])
def view_comments_per_post(request, pk):
    
    """
    Returns comments in the post in id pk
    """
    
    update_posts_expiration()
    #get comments on a certain post with the post id
    comments = Comment.objects.filter(post = pk)
    serializer = ViewCommentSerializer(comments, many=True)
    return Response(serializer.data)



