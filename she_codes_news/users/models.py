from django.db import models


from django.contrib.auth.models import AbstractUser

# class NewsStory(models.Model):    
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=200)   
#     author = models.ForeignKey(
#         get_user_model(),
#         on_delete=models.CASCADE
#     )    
# pub_date = models.DateTimeField()    
# content = models.TextField()

from django.contrib.auth.models import AbstractUser

class CustomUser (AbstractUser):
    pass

    def _str_(self):
        return self.username
