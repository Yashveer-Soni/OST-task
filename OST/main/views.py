from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method=="POST":
        files=request.FILES.get('files')
        print(files)
    return render(request, 'main/index.html')
