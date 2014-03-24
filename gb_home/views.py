# Create your views here.
from django.shortcuts import render
import os
from __builtin__ import file
from my_blog.settings import PDF_PATH
from django.http import HttpResponse


def home(request):
    return render(request, "testing-home.html") # had home.html there, testing out the sidebar

def contact(request):
    return render(request, "contact.html")

def social(request):
    return render(request, "social.html")

def pdf(request, filename):

    fullpath = os.path.join(PDF_PATH, filename)

    response = HttpResponse(file(fullpath).read())
    response['Content-Type'] = 'application/pdf'
    response['Content-disposition'] = 'attachment'
    return response

