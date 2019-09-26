from django.shortcuts import render, redirect
from apps.user_mng.models import User, Role
import bcrypt

def viewAdminLogin(req):
  if req.session.get("uid"):
    return redirect("/admin/dashboard/")
  if req.session.get("role_key") == 3:
    return redirect("/login/user/")
  return render(req, "log_reg/admin_login.html")

def viewUserLogin(req):
  if req.session.get("uid"):
    return redirect("/post/")
  return render(req, "log_reg/user_login.html")

def conAdminLogin(req):
  if req.method == "POST" and User.objects.isLoginValid(req):
    user = User.objects.get(email = req.POST.get("inputEmail"))
    if user.role_key.key == 3:
      return redirect("/login/user/")
    req.session["uid"] = User.objects.get(email = req.POST.get("inputEmail")).id
    req.session["role_key"] = User.objects.get(email = req.POST.get("inputEmail")).role_key.key
    return redirect("/admin/dashboard/")
  return redirect("/login/admin/")

def conUserLogin(req):
  if req.method == "POST" and User.objects.isLoginValid(req):
    req.session["uid"] = User.objects.get(email = req.POST.get("inputEmail")).id
    req.session["role_key"] = 3
    return redirect("/post/")
  return redirect("/login/user/")

def conLogout(req):
  req.session.clear()
  return redirect("/")

def viewRegister(req):
  return render(req, "log_reg/user_reg.html")

def conRegister(req):
  if req.method == "POST" and User.objects.isAddValid(req):
    User.objects.create(
      email = req.POST["inputEmail"],
      pwd = bcrypt.hashpw(req.POST["inputPassword"].encode(), bcrypt.gensalt()),
      nicename = req.POST["inputNiceName"],
      display_name = req.POST["inputDisName"],
      role_key = Role.objects.get(key = 3),
    )
    req.session["uid"] = User.objects.get(email = req.POST.get("inputEmail")).id
    req.session["role_key"] = 3
    return redirect("/post/")
  return redirect("/login/register/")