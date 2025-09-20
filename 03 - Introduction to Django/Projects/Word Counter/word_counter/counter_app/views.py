from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'pages/home.html')     # Shows form

def count(request):
     text = request.POST['text']  # get text from the form
     words = text.split()  # split by space
     word_count = len(words)  # count words
     return render(request, 'pages/home.html', {'text': text, 'word_count': word_count})
