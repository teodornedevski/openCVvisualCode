from django.http import HttpResponse
from django.shortcuts import render, redirect 
from .forms import *
from .shapedet_simp import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def image_view(request): 
  
    if request.method == 'POST': 
        form = Image(request.POST, request.FILES) 
        imageSearch()
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = Image() 
    return render(request, 'insertImage.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfuly uploaded') 

def drawing (request):
    return HttpResponse('was just testing is all')