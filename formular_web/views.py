
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import formset_factory
from django.urls import reverse
from django.utils.datetime_safe import strftime

from .forms import CarForm
from django.views import View


def home_view(request):
    # print(request.GET)
    return render(request, "home.html")


class CarFormView(View):
    # We are creating a formset out of the ContactForm
    Car_FormSet = formset_factory(CarForm)
    # The Template name where we are going to display it
    template_name = "home.html"

    # Overiding the get method
    def get(self, request, *args, **kwargs):
        # Creating an Instance of formset and putting it in context dict
        context = {
            'car_form': self.Car_FormSet(),
        }

        return render(request, self.template_name, context)

    #car_formset is set of all submitted cars and one identified user
    #it means that every itteration in car_formset marked as car, represents data for every submitted car
    #in every itteration of our form is also data of our submitter but this section (user) is not repeatable section
    #it means that although in every iteration of car is presented submiter but only in first itteration these data are not null
    #in every other itteration of car, submitter data are null
    #example result of 2 submitted cars:

    #simon
    #drienik
    #sdrienik @ gmail.com
    #EJ4746345
    #toyota
    #TRUCK
    #ba44444
    #29 - Sep - 22
    #5.0
    #== == == == == == == == == == == == == == == == == =
    #null
    #null
    #null
    #null
    #ford
    #personal
    #ba66666
    #26 - Sep - 2024
    #6.0

    def post(self, request, *args, **kwargs):
        car_formset = self.Car_FormSet(self.request.POST)
        if car_formset.is_valid():
            for car in car_formset:
                cd = car.cleaned_data
                print(cd.get('first_name'))
                print(cd.get('second_name'))
                print(cd.get('email'))
                print(cd.get('ID_number'))
                print(cd.get('car_brand'))
                print(cd.get('car_type'))
                print(cd.get('spz'))
                print(cd.get('registration_date').strftime("%d-%b-%y"))
                print(cd.get('vin'))
                print('===================================')

            context = {
                'car_form': self.Car_FormSet(),
                'error_message': ""
            }

            return render(request, self.template_name, context)
        else:
            context = {
                'car_form': self.Car_FormSet(),
                'error_message': car_formset.errors
            }
            return render(request, self.template_name, context)
