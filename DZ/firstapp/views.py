from django.shortcuts import render
from firstapp.models import PhoneBrand, Phone
from django.views import generic

def index(request):
    return render(request, 'index.html', {})


#def DB(request):
    #return render(request, 'DB.html', {})


class DB(generic.ListView):
    model = PhoneBrand
    context_object_name = 'PhoneBrand'
    template_name = 'DB.html'
