from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from .models import Profile


# Create your views here.


def user_list1():
    pass


def profile(request):
    user_details = Profile.objects.all().values('user').distinct()
    if 'user_details' in request.GET:
        user_details = 'user_details' in request.POST and request.POST['user_details']
        user_list = Profile.objects.filter(Q(user__contains='user_details'))
    return render(request, 'registration/profile.html', {'userlist':user_list1 })


def view(response):
    return render(response, "registration/view.html", {})


def signup(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/signup")
    else:
        form = RegisterForm()

    return render(response, "registration/signup.html", {"form": form})
