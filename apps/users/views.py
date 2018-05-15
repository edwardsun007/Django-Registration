from django.shortcuts import render, redirect  # for redirect
from django.contrib import messages   # for display flash message on page

# index method will be called from url.py
# it render templates   new_user/index.html .
def index(request):
    if "users" not in request.session:
        request.session["users"] = []  # if its first time user access this website, then we initiate session array
    return render(request,"users/index.html")

'''
remember in Django you need to determine
if get or post yourself
'''
def users(request):
    if request.method == "POST":
        #messages.info(request,"")
        new_user = {
            "gender":request.POST.get("gender"),
            "first_name":request.POST.get("fist_name"),
            "last_name":request.POST.get("last_name"),
            "email":request.POST.get("email"),
            "password":request.POST.get("password")
        } # because there is no data, create empty dict to store some fake user
        #new_user["email"] = request.POST.get("email") # we create data first
        #new_user["first_name"]=request.POST.get("first_name")
        #new_user["last_name"]=request.POST.get("last_name")
        #new_user["password"]=request.POST.get("password")
        valid = True
        if new_user["email"]=="":
            messages.error(request, "Email cannot be empty !") 
            valid = False
        if new_user["first_name"]=="":
            messages.error(request, "first_name cannot be empty !")
            valid = False
        if new_user["last_name"]=="":
            messages.error(request, "last_name cannot be empty !")
            valid = False
        if new_user["password"]=="":
            messages.error(request, "password cannot be empty !")
            valid = False

        for user in request.session["users"]:  
            if user["email"] == new_user["email"]:  ## if email already registered
                valid=False
                messages.error(request, "Email already used!")

        if valid == True: 
            users = request.session["users"]
            users.append(new_user)
            request.session["users"] = users # lets try 
            # IMPORTANT:  request.session is dictionary,  users is array
            request.session.modified = True
            messages.success(request,"Registered a user successfully!") # standard way of show success message
    return redirect("/")
        #By default, Django only saves to the session database when the session has been modified – that is if any of its dictionary values have been assigned or deleted:
        #for i in request.session["user"]:   
        #elif request.method == "GET":
        #print("This is get method!")

def all_users(request):
    current_users = request.session["users"]
    context = {
        "users":current_users
    }
    return render(request, "users/all_users.html", context)

## remember it takes a parameter called email
def show(request,email):
    for user in request.session["users"]:
        if user["email"] == email:
            current_user = user
    context = {
        "current_user":current_user
    }
    return render(request, "users/show.html", context)