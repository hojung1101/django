from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import  render


def index(request):
   return render(request, 'board/index.html', {'name': '유저'})
