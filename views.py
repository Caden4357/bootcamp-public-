from django.shortcuts import render, redirect
from .models import Panda
def index(request):
    context = {
        'all_pandas': Panda.objects.all()
    }
    
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        new_panda = Panda.objects.create(name = request.POST['name'], age = request.POST['age'], favorite_food = request.POST['food'], kungfu = request.POST['kungfu'] )
    return redirect('/')

def panda_profile(request, panda_id):
    context = {
        "this_panda": Panda.objects.get(id=panda_id)
    }
    return render(request, "panda_profile.html", context)