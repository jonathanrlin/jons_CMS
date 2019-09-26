from django.shortcuts import render, redirect
from apps.user_mng.models import User, Role
import bcrypt

def setRole():
  Role.objects.all().delete()
  Role.objects.create(
    key = 0,
    name = "Root"
  )
  Role.objects.create(
    key = 1,
    name = "Admin"
  )
  Role.objects.create(
    key = 2,
    name = "Author"
  )
  Role.objects.create(
    key = 3,
    name = "User"
  )


def init():
  User.objects.create(
    email = "root@g.c",
    pwd = bcrypt.hashpw("asdfasdf".encode('utf-8'), bcrypt.gensalt()),
    nicename = "nicename of root",
    display_name = "display name of root",
    role_key = Role.objects.get(key = 0)
  )

# setRole()
# init()

def viewAllUsers(req):
  if req.session.get("role_key") == 3:
    return redirect("/login/user/")
  if not req.session.get("uid"):
    return redirect("/login/admin/")
  return render(req, "user_mng/allUsers.html", {
    "all_users": User.objects.all()
  })

def viewDetailUser(req, user_id):
  if req.session.get("role_key") == 3:
    return redirect("/login/user/")
  if not req.session.get("uid"):
    return redirect("/login/admin/")
  if not User.objects.filter(id = user_id):
    return redirect("/admin/user/")
  return render(req, "user_mng/detailUser.html", {
    "user": User.objects.get(id = user_id)
  })

def viewAddUser(req):
  if req.session.get("role_key") == 3:
    return redirect("/login/user/")
  if not req.session.get("uid"):
    return redirect("/login/admin/")
  return render(req, "user_mng/addUser.html",{
    "all_roles": Role.objects.exclude(key = 0).order_by("-key")
  })

def conAddUser(req):
  if req.method == "POST" and req.session.get("uid"):
    if not User.objects.isAddValid(req):
      return redirect("/admin/user/new/")
    User.objects.create(
      email = req.POST["inputEmail"],
      pwd = bcrypt.hashpw(req.POST["inputPassword"].encode(), bcrypt.gensalt()),
      nicename = req.POST["inputNiceName"],
      display_name = req.POST["inputDisName"],
      role_key = Role.objects.get(key = int(req.POST["inputRoleKey"])),
    )
  return redirect("/admin/user/")

def viewEditUser(req, user_id):
  if req.session.get("role_key") == 3:
    return redirect("/login/user/")
  if not req.session.get("uid"):
    return redirect("/login/admin/")
  return render(req, "user_mng/editUser.html", {
    "user": User.objects.get(id = user_id),
    "all_roles": Role.objects.all().order_by("-key")
  })

def conEditUser(req):
  if (req.method == "POST" and
        User.objects.filter(id = req.POST.get("inputId")) and
        req.session.get("uid")):
    if not User.objects.isEditValid(req):
      url = "/admin/user/edit/" + req.POST.get("inputId") + "/"
      return redirect(url)
    user = User.objects.get(id = int(req.POST.get("inputId")))
    user.nicename = req.POST.get("inputNiceName")
    user.display_name = req.POST.get("inputDisName")
    user.pwd = req.POST.get("inputPassword")
    user.role_key = Role.objects.get(key = int(req.POST["inputRoleKey"]))
    user.save()

    url = "/admin/user/" + req.POST.get("inputId") + "/"
    return redirect(url)
  return redirect("/admin/user/")

def conDelUser(req):
  if(req.method == "POST" and req.session.get("uid") and
      User.objects.filter(id = int(req.POST.get("inputId")))):
    User.objects.get(id = int(req.POST.get("inputId"))).delete()
  return redirect("/admin/user/")