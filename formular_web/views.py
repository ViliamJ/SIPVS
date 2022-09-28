from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .forms import carForm
from django.shortcuts import render


def home_view(request):
    # print(request.GET)
    return render(request, "home.html")


def person_view(request):
    return render(request, "person_form_template.html")





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
                print(request.POST)
                data = request.POST['spz']
                return HttpResponse(f"{str(data)} + NICE")

                # username = request.POST["user"]
                # password = request.POST["pass"]
                # dict = {
                #    'username': username,
                #    'password': password
                # }
                # return render(request, 'validate.html', dict)

                # if a GET (or any other method) we'll create a blank form
    else:
        form = carForm()

    return render(request, 'car_from_template.html', {'form': form})


from django.forms import formset_factory
from .forms import ContactForm
from django.views import View

class ContactFormView(View):
    #We are creating a formset out of the ContactForm
    Contact_FormSet=formset_factory(ContactForm)
    #The Template name where we are going to display it
    template_name="home.html"

    #Overiding the get method
    def get(self,request,*args,**kwargs):
        #Creating an Instance of formset and putting it in context dict
        context={
                'contact_form':self.Contact_FormSet(),
                }

        return render(request,self.template_name,context)