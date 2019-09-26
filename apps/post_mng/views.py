from django.shortcuts import render, redirect
from django.db.models import Q
from apps.post_mng.models import Post
from apps.user_mng.models import User

def viewAllPosts(req):
  if not req.session.get("uid"):
    return redirect("/admin/login/")
  if req.session.get("uid") == 3:
    return redirect("/user/login")
  return render(req, "post_mng/index.html", {
    "all_posts": Post.objects.all()
  })

def viewAddPost(req):
  if not req.session.get("uid"):
    return redirect("/admin/login/")
  if req.session.get("uid") == 3:
    return redirect("/user/login")
  return render(req, "post_mng/addPost.html",{
    "all_authors": User.objects.filter(
      Q(role_key__key = 1) | Q(role_key__key = 2)
    )
   })

def viewEditPost(req, post_id):
  if not req.session.get("uid"):
    return redirect("/admin/login/")
  if req.session.get("uid") == 3:
    return redirect("/user/login")
  if not Post.objects.filter(id = post_id):
    return redirect("/admin/post/")
  return render(req, "post_mng/editPost.html", {
    "all_authors": User.objects.filter(
      Q(role_key__key = 1) | Q(role_key__key = 2)
    ),
    "post": Post.objects.get(id = post_id)
  })

def conAddPost(req):
  if req.method == "POST" and req.session.get("uid") and req.session.get("uid") != 3:
    if not Post.objects.isAddValid(req):
      return redirect("/admin/post/new/")
    Post.objects.create(
      title = req.POST.get("inputTitle"),
      author = User.objects.get(id = req.POST.get("inputAuthor")),
      content = req.POST.get("inputContent"),
      post_status = req.POST.get("inputVisi"),
      publish_date = req.POST.get("inputPubDate"),
    )
  return redirect("/admin/post/")

def conEditPost(req):
  if req.method == "POST" and req.session.get("uid") and req.session.get("uid") != 3:
    if not Post.objects.isAddValid(req):
      url = "/admin/post/edit/" + req.POST.get("inputPostId") + "/"
      return redirect(url)
    if not Post.objects.filter(id = req.POST.get("inputPostId")):
      return redirect("/admin/post/")
    post = Post.objects.get(id = req.POST.get("inputPostId"))
    post.title = req.POST.get("inputTitle")
    post.author = User.objects.get(id = req.POST.get("inputAuthor"))
    post.content = req.POST.get("inputContent")
    post.post_status = req.POST.get("inputVisi")
    post.publish_date = req.POST.get("inputPubDate")
    post.save()
  return redirect("/admin/post/")

def conDelPost(req):
  if req.session.get("uid") and req.method == "POST" and req.session.get("uid") != 3:
    Post.objects.get(id = int(req.POST.get("inputId"))).delete()
  return redirect("/admin/post/")