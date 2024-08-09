from django.http import HttpResponse    # added by Bryan

from django.shortcuts import render

# Create your views here.

# Each view should be a function

"""
def index(request):    #request: http request
    return HttpResponse("Hello!")
"""
# New version
def index(request):    #request: http request
    return render(request, "hello/index.html") #not to render just a string, but an entire html file (i.e. a template)! we put index in the hello folder, to avoid conflict if other index files

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!")

"""
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
"""
# New version, to render an entire page
def greet(request, name):
    return render(request, "hello/greet.html", {    #this third argument is called the context; i.e. all the information I would like to provide to the template e.g. variables
        "name": name.capitalize()     #I am passing a dictionary to the template!!
    })  


