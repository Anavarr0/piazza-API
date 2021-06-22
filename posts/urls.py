from django.urls import path
from . import views
from .views import *

 
urlpatterns = [
    path('posts-list/', all_posts_list), #returns all the posts, expired or not
    path('posts-list/<pk>/', posts_per_topic_all), #returns all the posts per topic pk
    path('expired-posts/', expired_posts_list), #Returns all expired posts
    path('expired-posts/<pk>/', expired_posts_per_topic_list), #Returns expired posts in topic pk
    path('not-expired-posts/', not_expired_post_list), #returns all the posts that aren't expired
    path('not-expired-posts/<pk>/', not_expired_posts_per_topic_list), #Returns not expired posts in topic pk
    path('most-active-post/<pk>/', most_active_post), #returns post with most likes and dislikes in topick pk
    path('post-new/', post_new), #posts a new post in database
    path('comment/<pk>/', comment_post), #add a comment to post with id pk
    path('like-post/<pk>/', like), #if the method used is POST it likes the post with id=pk
    path('dislike-post/<pk>/', dislike), #if the method used is POST it dislikes the post with id=pk
    path('search-comments/<pk>/', view_comments_per_post) #views with comments in a specific post with id=pk


]

