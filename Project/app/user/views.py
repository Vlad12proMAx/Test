from django.contrib import auth 
from django.urls import reverse
from django.shortcuts import redirect, render
from user.forms import UserLoginForm,UserRegistForm,UserProfileForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST) 
        if form.is_valid():  
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password) 
            if user:
                auth.login(request, user) 
                return redirect(reverse("main:index")) 
    else:
        form = UserLoginForm()

    context = {
        "title": "Авторизация",
        "form": form,
    }
    return render(request, "user/login.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegistForm(data=request.POST) 
        if form.is_valid(): 
            form.save() #сохраняем(Заносим в БД)
            user = form.instance #Пристваиваем форму пользователся 
            auth.login(request, user) #request содержит инфо 
            return redirect(reverse("user:profile"))
    else:
        form = UserRegistForm()


    context = {"title": "Регистирация",
               'form':form
               }
    return render(request, "user/registration.html", context)


def profile(request):

    if request.method == "POST":
        form = UserProfileForm(data=request.POST,instance=request.user,files = request.FILES)
        if form.is_valid():
            form.save()#Заносим в БД(если внес изменения)
            return redirect(reverse("user:profile")) 
    else:
        form = UserProfileForm(instance=request.user )


    context = {"title": "Профиль",
               'form':form,
               }
    return render(request, "user/profile.html", context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))

def user_carts(request):
    return render(request, 'user/user_carts.html')
