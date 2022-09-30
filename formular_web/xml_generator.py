from xml.dom import minidom
from django.forms import formset_factory
from formular_web.forms import CarForm


def generateXML(car_formset: formset_factory(CarForm)):
    root = minidom.Document()

    registration = root.createElement('registration')
    root.appendChild(registration)

    # USER
    user = root.createElement('user')
    registration.appendChild(user)

    first_name = root.createElement('first_name')
    user.appendChild(first_name)

    second_name = root.createElement('second_name')
    user.appendChild(second_name)

    email = root.createElement('email')
    user.appendChild(email)

    ID_number = root.createElement('ID_number')
    user.appendChild(ID_number)

    # CAR_LIST
    car_list = root.createElement('car_list')
    registration.appendChild(car_list)

    first = True
    for car in car_formset:
        cd = car.cleaned_data
        if first:
            first_name.appendChild(root.createTextNode(cd.get('first_name')))
            second_name.appendChild(root.createTextNode(cd.get('second_name')))
            email.appendChild(root.createTextNode(str(cd.get('email'))))
            ID_number.appendChild(root.createTextNode(cd.get('ID_number')))
            first = False

        # CAR
        car = root.createElement('car')
        car_list.appendChild(car)

        car_brand = root.createElement('car_brand')
        car.appendChild(car_brand)
        car_brand.appendChild(root.createTextNode(cd.get('car_brand')))

        car_type = root.createElement('car_type')
        car.appendChild(car_type)
        car_type.appendChild(root.createTextNode(cd.get('car_type')))

        spz = root.createElement('spz')
        car.appendChild(spz)
        spz.appendChild(root.createTextNode(cd.get('spz')))

        registration_date = root.createElement('registration_date')
        car.appendChild(registration_date)
        registration_date.appendChild(root.createTextNode(str(cd.get('registration_date'))))

        vin = root.createElement('vin')
        car.appendChild(vin)
        vin.appendChild(root.createTextNode(str(cd.get('vin'))))

    xml_str = root.toprettyxml(indent="\t")
    save_path_file = "registration.xml"

    with open(save_path_file, "w") as f:
        f.write(xml_str)
