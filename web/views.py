from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect

from forms import SearchForm
from django.db.models import Q

from api.models import BdbBiomarker, BdbAttrib
from tables import BdbBiomarkerTable, BdbAttribTable
from django_tables2 import RequestConfig
    

def page_search(request):
    if request.method == 'POST': 
        form = SearchForm(request.POST) 
        if form.is_valid(): 
            search_term = form.cleaned_data['search_term']
            table = BdbAttribTable(BdbAttrib.objects.filter(Q(value__icontains=search_term)|Q(bdbbiomarker__name__icontains=search_term)))
    else:
        form  = SearchForm() # An unbound form
        table = BdbBiomarker.objects.all()
    

    return render(request, 'page_search.html', {
        'form': form,
        "biomarkers": table,
    })

# Create your views here.
