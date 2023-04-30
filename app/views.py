from django.shortcuts import render

from app.models import New

# Create your views here.
def index (request):
    return render(request,'index.html')


def news(request):
    news=New.objects.all()

    context={
        'news':news,
        'news1':news.first()
    }
    return render(request,'news.html',context)


def newsSingle(request,id):
    news=New.objects.filter(id=id)
    context={
        'news':news
    }
    return render(request,'newssingle.html',context,id)


 