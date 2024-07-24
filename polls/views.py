from django.shortcuts import render
# from django.http import HttpResponse
from datetime import date


posts = [
    {
    'author' : 'Yann_Alain',
    'title' : 'Tech Post',
    'content' : 'Actualité Ivoirienne sue la Technologie.',
    'post_date' : date.today()
    },
    
    {
    'author' : 'Grace-Séphora',
    'title' : 'Media Post',
    'content' : 'Actualité Ivoirienne sur le journalisme.',
    'post_date' : date.today()
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render (request,'polls/home.html', context)

def about(request):
    return render(request,'polls/about.html', {'title':'About'})

# def index(request):
#     return HttpResponse("Hello, world. J'espere que vous allez bien?")

# def day(request):
#     return HttpResponse("<h1>Aujourd'hui est le {} <h1> \n <h3> Mon programme est bien pré-établi dorénavant<h3>".format(date.today()))
    

