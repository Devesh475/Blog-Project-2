from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# Create your models here.
class Blogpost(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=50)
    # slug = models.SlugField(default='hello-world') # used for better urls hello world becomes hello-world
    slug = models.SlugField(unique=True,blank=False) # used for better urls hello world becomes hello-world

    content = models.TextField(max_length=2000, null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-publish_date', '-timestamp']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    
    def get_edit_url(self):
        return f"/blog/{self.slug}/edit"

    def get_delete_url(self):
        return f"/blog/{self.slug}/delete"