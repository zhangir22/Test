from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from amocrm import Contact, exceptions

def index(request,response_mock):
    response_mock.add(
        "GET", "https://test.amocrm.ru/api/v4/contacts", match_querystring=False, status=200, json=1
    )
    response_mock.add(
        "GET", "https://test.amocrm.ru/api/v4/contacts", match_querystring=False, status=200, json=2
    )

    contacts = list(Contact.objects.all())

def about(request):
    return HttpResponse('<h4>About</h4>')
