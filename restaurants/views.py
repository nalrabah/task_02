from django.shortcuts import render
from django import http
# Create your views here.
def taskfile(request):
    context = {
    "msg":"Hello World!",
    }
    return render(request, 'myfile.html', context)