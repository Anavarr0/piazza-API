from django.db import models

class Message(models.Model):
    userName = models.CharField(max_length=60)
    userMessage = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.userName, self.userMessage

    