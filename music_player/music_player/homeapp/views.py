from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    songs=Musics.objects.filter(status=0)
    return render(request,"forhome/index.html",{"song":songs})

def search(request):
    query = request.GET.get('query')
    song = Musics.objects.all()
    qs = song.filter(name__icontains=query)
    return render(request,'forhome/output.html', {"songs":qs})