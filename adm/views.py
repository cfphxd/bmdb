from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


# Create your views here.

def load_first(request):
    return HttpResponse('Nothing')

