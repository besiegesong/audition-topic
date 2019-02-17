# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response,HttpResponse
from win32com import client
from pydocx import PyDocX
from tools.testdocttoHtml import *
def home(request):
    return render_to_response('html/home.html')
def loadResume(request):
    #调用解析方法
    return HttpResponse(resolveResume())

def docTOdocx(filename):
    newFilename =filename+"c"
    word = client.Dispatch("Word.Application")
    doc = word.Documents.Open(filename)
    doc.SaveAs(newFilename, 16)
    doc.Close()
    word.Quit()
    return newFilename
