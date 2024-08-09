from django import forms #this is to create forms in web applications
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# row below not used anymore, because the list of tasks will now be saved within the user's session
tasks = ["foo", "bar", "baz"]    #global variable with all the tasks; visible accross the whole application

# We create a new class to represent a form for the web application
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)  # I can even add constraints!; this is called: client side validation

# Create your views here.

def index(request):
    if "tasks" not in request.session: #I am looking inside the session: is there already a list of tasks in that session?
        request.session["tasks"] = []  #If user does not have a list of task --> give an empty list of tasks
    return render(request, "tasks/index.html", {
       "tasks": request.session["tasks"]
       # "tasks": tasks     #the left part is the variable that Django will have access to when rendering the view
    })

def add(request):
    # This is for server side validation:
    if request.method == "POST":   # i.e. if the user submitted some form data
        form = NewTaskForm(request.POST)  #the form contains all the data that the user submitted
        if form.is_valid():   # did the user provide all the necessary information and in the right format
            task = form.cleaned_data["task"]    # to avoid an error, need to run in the terminal:    python manage.py migrate
            request.session["tasks"] += [task]   #adding a list that just contains the new task
            #tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))    #HttpResonseRedirect to go to the index page after adding a task;  Django's reverse() function to figure out what is the route
        else:   #i.e. if the form is not valid:
            return render(request, "tasks/add.html",{
                "form":form    #we still provide back to the user the form they submitted, so that they can make changes if they want to
            })

    return render(request, "tasks/add.html", {      #if the user just GET the page we just provide an empty form
        "form": NewTaskForm()      # this will be passed into the add.html template
     })