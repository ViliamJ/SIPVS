from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import formset_factory
from django.urls import reverse
from django.utils.datetime_safe import strftime

from .forms import CarForm
from django.views import View

from .html_generator import generateHTML
from .xml_generator import generateXML
from .xml_validator import validateXML
from django.http import HttpResponse


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

    # DATA work is now in xml_generator

    # car_formset is set of all submitted cars and one identified user
    # it means that every itteration in car_formset marked as car, represents data for every submitted car
    # in every itteration of our form is also data of our submitter but this section (user) is not repeatable section
    # it means that although in every iteration of car is presented submiter but only in first itteration these data are not null
    # in every other itteration of car, submitter data are null
    # example result of 2 submitted cars:

    # simon
    # drienik
    # sdrienik @ gmail.com
    # EJ4746345
    # toyota
    # TRUCK
    # ba44444
    # 29 - Sep - 22
    # 5.0
    # == == == == == == == == == == == == == == == == == =
    # null
    # null
    # null
    # null
    # ford
    # personal
    # ba66666
    # 26 - Sep - 2024
    # 6.0

    def post(self, request, *args, **kwargs):
        car_formset = self.Car_FormSet(self.request.POST)
        file_name = request.POST['file_name']
        xslt_name = request.POST['xslt_name']
        validate_message = ""

        if 'generate_validate_XML' in request.POST:

            try:
                validate_message = validateXML(file_name=file_name)
            except:
                return HttpResponse("Something went wrong, probably file you specified does not exist")
            if validate_message:
                return HttpResponse("Validated xml file is okey")
            else:
                return HttpResponse("Xml file is NOT okey." + validate_message)

        if 'generate_HTML' in request.POST:
            generated_html = generateHTML(file_name, xslt_name)
            return render(request, generated_html)

        if car_formset.is_valid():

            if 'generate_XML' in request.POST:

                generateXML(car_formset, file_name=file_name)
                context = {
                    'car_form': self.Car_FormSet(),
                    'error_message': "",
                    'validate_message': validate_message
                }

                return render(request, self.template_name, context)
        else:
            context = {
                'car_form': self.Car_FormSet(),
                'error_message': car_formset.errors,
                'validate_message': validate_message
            }
            return render(request, self.template_name, context)