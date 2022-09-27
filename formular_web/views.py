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

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .forms import carForm

def get_car(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = carForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            if 'generateXml' in request.POST:
                print(request.POST)
                return HttpResponse("generated")
            elif 'validateXml' in request.POST:
                return HttpResponse("validated")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = carForm()

    return render(request, 'car_from_template.html', {'form': form})