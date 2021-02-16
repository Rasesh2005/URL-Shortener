from django.shortcuts import render
from .models import *
# Create your views here.
def redirect(request,slug):
    params={
        "redirect_url":Connection.objects.filter(slug=slug)[0].redirect_url
    }
    print(params)

    return render(request,"redirect.html",context=params)

def index(request):
    if request.method=="POST":
        # print(request.POST)
        slug=request.POST.get('slug')
        redirect=request.POST.get('redirect')
        obj=Connection.objects.create(slug=slug,redirect_url=redirect)
        Connection.save(obj)
    return render(request,"index.html")