#File entirely created by Bryan

from django.urls import path

from . import views    # the dot means, from the current directory

app_name = "tasks"   # this is to avoid confusion on e.g. "index" who might be used in different applications of the same Web App!

#List of all accessible urls for this particular app
urlpatterns = [
    path("", views.index, name="index"),   #when someone visits the default route "" url, the function "index" is called; views.py is the file where the function index is; name is the id for the url in question
    path("add", views.add, name="add")
]
    