from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Links

def home(request):

    data = Links.objects.all()

    contex = {
        'data':data,
    }
    return render(request, 'home.html', contex)

def create_link(request):
    habar = ''
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        link = request.POST['link']
        if Links.objects.filter(link=link):
            habar = 'such information is available'
        else:
            baza = Links.objects.create(title=title, body=body, link=link)
            baza.save()
            return redirect('/')


    contex = {
        'habar':habar,
    }
    return render(request, 'create_link.html', contex)

def delete(request):
    data = Links.objects.all()
    contex = {
        'data':data,
    }
    return render(request, 'delete.html', contex)

def delete_link(request, pk):
    data = Links.objects.get(id=pk)
    data.delete()
    return redirect('/')

def update(request):
    yangilash = Links.objects.all()

    contex = {
        'yangilash':yangilash,
    }
    return render(request, 'update.html', contex)

def update_link(request, pk):
    data = get_object_or_404(Links, pk=pk)
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        link = request.POST['link']

        data.title = title
        data.body = body
        data.link = link
        data.save()
        return redirect('/', pk=data.id)
       
    contex = {
        'update_link':data,   
    }
    return render(request, 'update_link.html', contex)
   

