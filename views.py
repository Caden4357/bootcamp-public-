from django.shortcuts import render, redirect
from time import localtime, strftime
import random

def index(request):
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')

def process_money(request):
    if request.method =='POST':
        if request.POST['location'] == 'farm':
            request.session['gold'] += random.randint(10, 20)
        elif request.POST['location'] == 'cave':
            request.session['gold'] += random.randint(5, 10)
        elif request.POST['location'] == 'house':
            request.session['gold'] += random.randint(2, 5)
        elif request.POST['location'] == 'casino':
            request.session['gold'] += random.randint(-50, 50)
        elif request.POST['location'] == 'reset':
            request.session.flush()
    return redirect('/') 

#reset gold
# def reset(request):
#     if request.POST['location'] == 'reset':
#         request.session.flush()
#     return redirect('/')
