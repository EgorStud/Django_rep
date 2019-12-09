from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import User_login


def open_manager(request):
	return HttpResponse("привет, это страница менеджера:)")

def open_user(request):
	return HttpResponse("Привет,это страница Юзера:)")

def log_in(request):
	if request.method == "POST":
		form = User_login(request.POST)
		if form.is_valid():
			post = form.save()
			return HttpResponseRedirect(post.get_url())#'label_app/log_in/')
	else:
		form = User_login()
	return render(request,'label_app/login.html',{'form' : form})