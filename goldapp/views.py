from django.shortcuts import render, HttpResponse, redirect
import random


def index(request):
    return render(request, 'index.html')

def Farm(request):
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'text' not in request.session:
        request.session['text'] = []
    random_num = random.randint(1,10)
    request.session['total'] += random_num
    request.session['text'].append(f"you have earned {random_num} from the Farm")
    return redirect('/')

def Cave(request):
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'text' not in request.session:
        request.session['text'] = []
    random_num = random.randint(10,20)
    request.session['total'] += random_num
    request.session['text'].append(f"you have earned {random_num} from the Cave!")
    return redirect('/')

def House(request):
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'text' not in request.session:
        request.session['text'] = []
    random_num = random.randint(1,5)

    request.session['total'] += random_num
    request.session['text'].append(f"you have earned {random_num} from the House!")
    return redirect('/')

def Casino(request):
    plusminus = request.POST['location']
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'text' not in request.session:
        request.session['text'] = []
    random_num = random.randint(-50,50)
    request.session['total'] += random_num
    request.session['text'].append(f"you have earned {random_num} from the Casino!")
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')