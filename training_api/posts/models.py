from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=256)
    user_id = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
