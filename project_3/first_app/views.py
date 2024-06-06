from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d={'author' : 'rahim', 'age':20, 'lst' : ['python','is','best'],'birthday' :
       datetime.datetime.now(),'val' : '', 'courses' : [
        {
            'id' : 1,
            'course' : 'python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'course' : 'Django',
            'fee' : 10000
        },
        {
            'id' : 3,
            'course' : 'C',
            'fee' : 1000
        },
    ] }
    return render(request,'home.html',d)
