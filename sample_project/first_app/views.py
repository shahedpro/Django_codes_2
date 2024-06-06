from django.shortcuts import render
import datetime

def home(request):
    d = [
        {
            'title': 'My First Blog',
            'author': 'rahim',
            'created_at': datetime.datetime(2023, 5, 20),
            'content': 'This is the content of my first blog post. It is a great introduction to the world of blogging.'
        },
        {
            'title': 'Learning Django',
            'authoic design': 'Ali',
            'created_at': datetime.datetime(2023, 6, 15),
            'content': 'Django is a high-level Framework'
        },
        {
            'title': 'Advanced Python',
            'author': 'Sara',
            'created_at': datetime.datetime(2023, 7, 10),
            'content': 'we will explore advanced Python topics such as decorators, generators, and context managers.'
        }
    ]
    
    return render(request, 'home.html', {'home': d})
