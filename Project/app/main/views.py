from django.shortcuts import render

def index(request):

    context ={
        'title':'Главная', 
        'content':'Магазин мебели',
    }

    return render(request,'main/index.html',context)


def info(request):

    context ={
        'title': 'О нас', 
        'content':'Информация о нас',
        }

    return render(request,'main/info.html',context)

def сontact(request):

    context ={
        'title': 'Контактная информация',
        'content':"Номер:x-xxx-xxx-xx-xx" 
        }
    return render(request,'main/contact.html',context)