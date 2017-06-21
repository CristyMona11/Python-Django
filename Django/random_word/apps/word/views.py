from django.shortcuts import render,HttpResponse, redirect
import random

def index(request):
    return render(request, 'word/index.html')

def count(request):
    if request.method == 'POST':
        return redirect('/')

def generate(request):
    if 'counter' not in request.session:
        request.session['counter']=1
    else:
        request.session['counter']+=1
    word = ''
    my_letters = ['a',str(1), 'b',str(2), 'c', str(4), 'd',str(7), 'e',str(6), 's',str(3), 't',str(9),str(8), 'z', 'u', 'o', 'x', 'A', 'B','C', 'D', 'R', 'Y', 'P']
    for times in range (0, 14):
        word = word + str(random.choice(my_letters))
    words = {
        'random_word': word
    }
    return render(request, 'word/index.html', words)

def reset(request):
    request.session.clear()
    return redirect('/')
