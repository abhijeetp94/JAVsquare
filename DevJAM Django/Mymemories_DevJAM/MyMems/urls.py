from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = "index"),
    path('productivity/',views.productivity, name = "productivity"),
    path('images/',views.images, name = "images"),
    path('dairy/',views.dairy, name = "dairy"),
    path('mistakes/',views.mistakes, name = "mistakes"),
    path('goals/',views.goals, name = "goals"),
    path('login/',views.login, name = "login"),
    path('signup/',views.signup, name = "signup"),
    path('signupsuccess/',views.signupsuccess, name = "signupsuccess"),
    path('upload/',views.upload, name = "uploaded"),
]