from django.db import models
from django.contrib import messages
from django.contrib.messages import get_messages
import bcrypt
import re

class UserManager(models.Manager):
  def isAddValid(self, req):
    if len(req.POST.get("inputNiceName")) < 2:
      messages.error(req, "Nice name should be at least 2 characters")

    if len(req.POST.get("inputDisName")) < 2:
      messages.error(req, "Display name should be at least 2 characters")

    EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if not EMAIL_REGEX.match(req.POST.get("inputEmail")):
      messages.error(req, "Invalid email")

    if User.objects.filter(email = req.POST.get("inputEmail")):
      messages.error(req, "Email is already taken")

    if len(req.POST.get("inputPassword")) < 8:
      messages.error(req, "Password should be at least 8 characters")

    if req.POST.get("inputPassword") != req.POST.get("inputConPassword"):
        messages.error(req, "Password must match confirm password")

    if req.POST.get("inputRoleKey") and (int(req.POST.get("inputRoleKey")) < 0 or
          int(req.POST.get("inputRoleKey"))) > 3:
        messages.error(req, "Please don't hack the website")

    storage = messages.get_messages(req)
    storage.used = False
    return len(storage) == 0

  def isEditValid(self, req):
    if len(req.POST.get("inputNiceName")) < 2:
      messages.error(req, "Nice name should be at least 2 characters")

    if len(req.POST.get("inputDisName")) < 2:
      messages.error(req, "Display name should be at least 2 characters")

    EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if not EMAIL_REGEX.match(req.POST.get("inputEmail")):
      messages.error(req, "Invalid email")

    if (User.objects.get(id = int(req.POST.get("inputId"))).email !=
        req.POST.get("inputEmail")):
      messages.error(req, "Please don't hack the website")

    if len(req.POST.get("inputPassword")) < 8:
      messages.error(req, "Password should be at least 8 characters")

    if req.POST.get("inputPassword") != req.POST.get("inputConPassword"):
        messages.error(req, "Password must match confirm password")

    if (int(req.POST.get("inputRoleKey")) < 0 or
          int(req.POST.get("inputRoleKey"))) > 3:
        messages.error(req, "Please don't hack the website")

    storage = messages.get_messages(req)
    storage.used = False
    return len(storage) == 0


  def isLoginValid(self, req):
    if not (len(req.POST.get("inputPassword")) > 7 and
      User.objects.filter(email = req.POST.get("inputEmail")) and
      bcrypt.checkpw(
        req.POST.get("inputPassword").encode('utf-8'),
        User.objects.get(email = req.POST.get("inputEmail")).pwd.encode('utf-8')
      )
    ):
      messages.error(req, "The email and password you entered did not match our records. Please double-check and try again.")
    storage = messages.get_messages(req)
    storage.used = False
    return len(storage) == 0

class Role(models.Model):
  key = models.IntegerField()
  name = models.CharField(max_length=20)

class User(models.Model):
  email = models.CharField(max_length=100)
  pwd = models.CharField(max_length=255)
  nicename = models.CharField(max_length=50)
  display_name = models.CharField(max_length=250)
  role_key = models.OneToOneField(Role)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()