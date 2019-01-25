from django.http import HttpResponse
from django.shortcuts import render
import random

def index(request):
    return HttpResponse("hello!!")
    
def html_tag(request):
    s="<h1>안녕하세요!</h1>"
    return HttpResponse(s)
    
def dinner(request):
    menu=["떡볶이", "파스타", "닭갈비", "짜장면"]
    return HttpResponse(random.choice(menu))
    
def lotto(request):
    return HttpResponse(random.sample(range(1,46),6))
    
def html_file(request):
    return render(request, "html_file.html")