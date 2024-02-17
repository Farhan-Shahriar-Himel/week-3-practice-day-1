from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {
        'name': 'farhan',
        'age': 21,
        'favorite_books': ['python for beginners', 'data science in python', 'machine learning in python'],
        'date': datetime.datetime.now(),
        'lst' : [
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
        ]
    }
    return render(request, 'first_app/home.html', d)