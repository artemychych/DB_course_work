from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.

from kursach.models import Biom


def showdata(request):
    results = Biom.objects.all()
    print(results)
    return render(request, 'home.html', {'data': results})


def auth(request):
    if not request.user.is_authenticated:
        is_active = 'true'
        wrong_info = 'false'
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    is_active = 'false'
            else:
                wrong_info = 'true'
    else:
        return redirect('home')
    return render(
        request, 'auth.html', {'is_active': is_active, 'wrong_info': wrong_info}
    )


