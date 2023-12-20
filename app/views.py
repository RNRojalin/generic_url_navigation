from django.shortcuts import render

# Create your views here.
def convo1(request):
    return render(request,'convo1.html')

def convo2(request):
    return render(request,'convo2.html')