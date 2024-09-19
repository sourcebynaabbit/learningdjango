from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    currenttime = datetime.now()
    hour = currenttime.hour
    if 5 <= hour < 12:
        greeting = 'Good morning'
    elif 12 <= hour < 17:
        greeting = 'Good afternoon'
    else:
        greeting = 'Good evening'
    
    namesdata = names()
    context = {'currenttime': currenttime, 'msg': greeting, 'names': namesdata}
    return render(request, 'index.html', context)

def names():
    context={}
    context["petnames"]=['boxer','french-bulldog','vodaphone-dog']
    return context["petnames"]

def signup(req):
    return render(req,'signup.html')

def signin(req):
    return render(req,'signin.html')

def testing(req):
    username='admin'
    return render(req,'testing.html',{'username':username})

def displayproducts(req):
    context = {}
    context['allproducts'] = [
        {'name': 'samsung', 'price': 10000, 'ram': '8GB', 'category': 'mobile'},
        {'name': 'iPhone', 'price': 12000, 'ram': '6GB', 'category': 'mobile'},
        {'name': 'Dell XPS', 'price': 15000, 'ram': '16GB', 'category': 'laptop'},
        {'name': 'Sony TV', 'price': 8000, 'ram': 'N/A', 'category': 'television'},
        {'name': 'Pixel', 'price': 9000, 'ram': '8GB', 'category': 'mobile'},
        {'name': 'MacBook Pro', 'price': 18000, 'ram': '32GB', 'category': 'laptop'},
    ]
    return render(req, 'products.html', context)