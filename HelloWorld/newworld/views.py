from django.shortcuts import render

# Create your views here.
#coding:utf-8
def index(request):
       return render(request,"index.html",)
