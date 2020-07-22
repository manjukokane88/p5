from django.shortcuts import render


def first(request):
    return render(request,'demo/first.html', context={'data':'Manju','name':'rohit'})

def second(request):
    fruits=['apple','mango','orange','kiwi','Banana','strabary']
    return render(request,'demo/second.html',{'fruits':fruits})

def thrid(request):
    return render(request,'demo/thrid.html',{'a':20 ,'b':35})    
