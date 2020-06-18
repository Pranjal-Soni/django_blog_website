from django.shortcuts import render

# Create your views here.

posts =[
    {
        'author':'Pranjal',
        'title': 'Blog Post one',
        'Content':'FIrst post Content',
        'Date' : 'May 25, 2020'
    },
    {
        'author':'Pranjal',
        'title': 'Blog Post two',
        'Content':'FIrst post Content',
        'Date' : 'May 25, 2020'
    },
    {
        'author':'Pranjal',
        'title': 'Blog Post Three',
        'Content':'FIrst post three',
        'Date' : 'May 25, 2020'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html',context)

def About(request):
    return render(request,'blog/about.html',{'title':'About'})
