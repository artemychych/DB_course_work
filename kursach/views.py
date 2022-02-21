from django.shortcuts import render

# Create your views here.

from kursach.models import Biom


def showdata(request):
    results = Biom.objects.all()
    print(results)
    return render(request, 'Index.html', {'data': results})

