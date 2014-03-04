from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def load_page_search(request):
    t = get_template('page_search.html')
    html = t.render(Context({'':''}))
    return HttpResponse(html)




# Create your views here.
