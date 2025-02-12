from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        titulo = request.POST.get('titulo')    
        video = request.FILES.get('video')
