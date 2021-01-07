from django.shortcuts import render
a=["-","Dark Blue","Black","Pistachio"]
b=["-","Совершенно новый цвет","Давно приевшийся","Почти новый цвет"]
c=["-","Темно голубо-синий", "Черный", "Фисташковый"]
def index(request):
    return render(request, 'index.html',{})
# Create your views here.
def detail(request, ID):
    return render(request, 'detail.html',{'X':a[ID],'B':b[ID], 'C':c[ID]

    })

