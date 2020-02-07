from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from pages import test2
import time, _thread

realval3 = 'settt'

# def main():
#     global realval3
#     realval3 = test2.main()
#     print('hereeee ' + realval3)
#
# # end function
# if __name__ == "__main__":
#     main()

def estimation_view(request, *args, **kwargs, ):
    context = {}
    upload = request.POST.get('upload', None)
    context['upload'] = upload
    context['my_list'] = test2.main()
    return render(request, "estimation.html", context)

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1> Hello World</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": " this is about me",
        "my_number": 123,
        "my_list" : [1223, 3434 ,3434 , 344 ]
    }
    return render(request, "contact.html", my_context)

def imageUpload_view(request, *args, **kwargs):
    context = {}
    login = request.POST.get('login', None)
    context['login'] = login
    return render(request, "uploadImage.html", context)

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def signIn_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def signUp_view(request, *args, **kwargs):
    return render(request, "register.html", {})

# def event(request):
#     context = {}
#     login = request.POST.get('login', None)
#     context['login'] = login
#     return render(request, 'event.html', context)

def temp_view(request, *args, **kwargs):

    my_context = {
        "my_text": " this is about me",
        "my_number": 123,
        "my_list" : test2.main()
    }
    return render(request, "temp.html", my_context)