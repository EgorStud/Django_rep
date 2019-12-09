from django.urls import path

from . import views

urlpatterns = [
	path('manager/',views.open_manager,name = 'open_manager'),
	path('user/',views.open_user,name = 'open_user'),
	path('log_in/',views.log_in,name = 'log_in')
]