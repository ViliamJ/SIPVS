from django.shortcuts import render


# Create your views here.

from django.shortcuts import render


def home_view(request):
    #print(request.GET)
    marha = request.GET
    print(marha)
    return render(request, "home.html")

def person_view(request):
    return render(request, "person_form_template.html")