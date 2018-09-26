from django.shortcuts import render,HttpResponse
from blog import models
# Create your views here.


def index(requests):
    if requests.method == "POST":
        dic_user = {}
        dic_user["username"] = requests.POST.get('username',None)
        dic_user["sex"] = requests.POST.get('sex',None)
        dic_user["age"] = requests.POST.get('age',None)
        models.UserInfo.objects.create(**dic_user)

    userlist = models.UserInfo.objects.all()
    return render(requests,'index.html',{"userlist":userlist})



def article(requests,y):
    return HttpResponse("years: "+y)
