# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse
from .models import Travel
import json
# Create your views here.
#添加标记
def addTravel(request):
    if request.method=="POST":
        location_x = float(request.POST.get("x").strip())
        location_y = float(request.POST.get("y").strip())
        text = str(request.POST.get("text").strip())
        Travel(location_x=location_x,location_y=location_y,text=text).save()
    return HttpResponse()
#获取标记
def getTravel(request):
    results = []
    for travel in Travel.objects.all():
        result=[]
        result=[travel.location_x,travel.location_y,travel.text]
        results.append(result)
    return HttpResponse(json.dumps(results))