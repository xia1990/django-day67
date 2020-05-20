#!/usr/bin/python3
#_*_ coding:utf-8 _*_
from django.shortcuts import  render,HttpResponse
from django.views import View
import os

#FBV
def index(request):
    return render(request,"index.html")

#CBV
class Index(View):
    def get(self,request):
        return render(request,"index.html")

    def post(self,request):
        return render(request,"index.html")


#上传文件
def upload(request):
    if request.method=="POST":
        #获取上传文件]
        myfile=request.FILES.get("myfile")
        #myfile.name：获取上传文件的文件名称
        with open(myfile.name,"wb") as f1:
            for chunk in myfile.chunks():
                f1.write(chunk)
        return HttpResponse("upload ok")
    else:
        return render(request,"upload.html")



