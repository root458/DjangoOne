from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Jason','title':'Home Page'})

def add(request):
    val1 = int(request.POST['num1'])    #use single quotation marks for the GET
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'result.html',{'result':res,'title':'Result Page'})