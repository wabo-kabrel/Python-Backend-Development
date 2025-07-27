from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'name': 'Lamar',
        'age': 19,
        'nationality': 'Cameroonian'}
    return render(request, 'index.html', context)