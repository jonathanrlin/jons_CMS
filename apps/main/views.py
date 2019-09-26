from django.shortcuts import render, redirect
from apps.main.models import Option
from apps.post_mng.models import Post

def init():
  Option.objects.all().delete()
  Option.objects.create(
    name = "blogname",
    value = "Sample Page"
  )
  Option.objects.create(
    name = "blogdescription",
    value = "A sample page of Jonathan's CMS"
  )

init()

def index(req):
  return render(req, "main/index.html")

def viewAllPosts(req):
  return render(req, "main/allPosts.html", {
    "blogname": Option.objects.get(name = "blogname").value,
    "blogdescription": Option.objects.get(name = "blogdescription").value,
    "all_posts":Post.objects.all()
  })

def viewOnePost(req, post_id):
  return render(req, "main/onePost.html", {
    "blogname": Option.objects.get(name = "blogname").value,
    "blogdescription": Option.objects.get(name = "blogdescription").value,
    "post":Post.objects.get(id = post_id)
  })