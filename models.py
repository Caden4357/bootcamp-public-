from django.db import models

class Panda(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    favorite_food = models.CharField(max_length = 50)
    kungfu = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Date many to many
    # Post one to many

# many to many relationship
class Date(models.Model):
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    pandas_on_date = models.ManyToManyField(Panda, related_name = "dates")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    content = models.TextField()
    posted_by = models.ForeignKey(Panda, related_name="posts", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)