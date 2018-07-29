
from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render (request,'home.html')
def about(request):
    return render(request,'about.html')
def count(request):
    ft=request.GET['textarea']
    wordlist=ft.split()
    wd={}
    for w in wordlist:
        if w in wd:
            wd[w]+=1
        else:
            wd[w]=1
    x=sorted(wd.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'textarera':ft,'count':len(wordlist),'dictn':x})
