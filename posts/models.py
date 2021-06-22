from django.db import models
from django.contrib.auth import settings
from django.utils import timezone
from django.contrib.auth.models import User


TOPICS = (("Health" , "Health"), ("Sports" , "Sports"), ("Politics" , "Politics"), ("Tech" , "Tech"))

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255, default=" ")
    body = models.CharField(max_length=255)
    topic = models.CharField(max_length=20, choices = TOPICS, default = "Tech")
    created_at = models.DateTimeField(default=timezone.now)
    expiration_time = models.DurationField()
    is_expired = models.BooleanField(default=False)
    likes_count = models.PositiveSmallIntegerField(default=0)
    dislikes_count = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return f"id: {self.id} - User: {self.user} - Message: {self.body} - Topic: {self.topic} - Created at: {self.created_at} - likes: {self.likes_count} - dislikes: {self.dislikes_count}"

       
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    post = models.ForeignKey(Post,  on_delete=models.CASCADE, default=None, related_name='comments')
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    

    def __str__(self):
        return f"User: {self.user} - Post_id: {self.post.id} - Message: {self.comment}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    liked_post = models.ForeignKey(Post,  on_delete=models.CASCADE, default=None)
    

    

    def __str__(self):
        return f"User: {self.user} - Post_id: {self.liked_post.id}"

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    disliked_post = models.ForeignKey(Post,  on_delete=models.CASCADE, default=None)

    

    def __str__(self):
        return f"User: {self.user} - Post_id: {self.disliked_post.id}"


