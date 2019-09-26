from django.db import models
from apps.user_mng.models import User
from django.contrib import messages
from django.contrib.messages import get_messages

class PostManager(models.Manager):
  def isAddValid(self, req):
    if len(req.POST.get("inputTitle")) == 0 :
      messages.error(req, "Title must not be empty.")
    if len(req.POST.get("inputContent")) == 0 :
      messages.error(req, "Content must not be empty.")

    storage = messages.get_messages(req)
    storage.used = False
    return len(storage) == 0

class Post(models.Model):
  title = models.CharField(max_length=255)
  author = models.ForeignKey(User, related_name="posts")
  content = models.TextField()
  post_status = models.CharField(max_length=20)
  publish_date = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = PostManager()