# Django imports
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

# Django plugins imports
from django_tables2 import RequestConfig

# App import
from forms import SearchForm
from api.models import *
from tables import BdbBiomarkerTable
    
def get_table(request, search_target, search_term):
    if(search_target=='All'):
        return BdbBiomarker.objects.filter(Q(name__icontains=search_term) | 
                    Q(bdbattrib__value__icontains=search_term) |
                    Q(dise__name__icontains=search_term) | 
                    Q(food__name__icontains=search_term) |
                    Q(phys__name__icontains=search_term) |
                    Q(fatt__name__icontains=search_term)
                ).distinct()
    elif(search_target=='Biomarker'):
        return BdbBiomarker.objects.filter(Q(name__icontains=search_term) |
                    Q(bdbattrib__value__icontains=search_term) 
                ).distinct()
    elif(search_target=='Food'):
        return BdbBiomarker.objects.filter(food__name__icontains=search_term)
        #return BdbFood.objects.filter(name__icontains=search_term)
    elif(search_target=='Disease'):
        return BdbBiomarker.objects.filter(dise__name__icontains=search_term)
        #return BdbDisease.objects.filter(name__icontains=search_term) 
    elif(search_target=='Pathway'):
        return BdbBiomarker.objects.filter(phys__name__icontains=search_term)
        #return BdbDisease.objects.filter(name__icontains=search_term)
    else:
        return BdbBiomarker.objects.all()


def page_search(request):
    if request.method == 'POST': 
        form = SearchForm(request.POST) 
        if form.is_valid(): 
            search_term = form.cleaned_data['search_term']
            search_target = form.cleaned_data['search_target']
            items = get_table(request, search_target, search_term)
    else:
        form  = SearchForm() # An unbound form
        items = BdbBiomarker.objects.all()
        search_target = ""
        search_term=""
    

    return render(request, 'page_search.html', {
        'form':   form,
        "items":  items,
        "tgt":    search_target,
        "sterm":  search_term,
    })

# Create your views here.
