from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homepage(request):
    print((request.method))
    # print((request.build_absolute_url()))
    print(request.build_absolute_uri())

    return HttpResponse("<h1>hi hello<h1>")
