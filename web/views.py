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

## HOME ##

def page_home(request):
    return render(request, 'page_home.html', {
        'tt':   1,
    })

## LOGIN ##




## ABOUT ##

def page_about(request):
    return render(request, 'page_about.html', {
        'tt':   1,
    })

def page_ab_contact_us(request):
    return render(request, 'page_ab_contact_us.html', {
        'tt':   1,
    })

def page_ab_terms(request):
    return render(request, 'page_ab_terms.html', {
        'tt':   1,
    })

## DATABASE ##

def page_database(request):
    return render(request, 'page_database.html', {
        'tt':   1,
    })

def page_db_search(request):
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


    return render(request, 'page_db_search.html', {
        'form':   form,
        "items":  items,
        "tgt":    search_target,
        "sterm":  search_term,
    })


def page_db_register(request):
    return render(request, 'page_db_register.html', {
        'tt':   1,
    })

def page_db_faq(request):
    return render(request, 'page_db_faq.html', {
        'tt':   1,
    })


## FOOD CLAIMS  ##

def page_food_claims(request):
    return render(request, 'page_food_claims.html', {
        'tt':   1,
    })

def page_fc_updates(request):
    return render(request, 'page_fc_updates.html', {
        'tt':   1,
    })

def page_fc_nz_info(request):
    return render(request, 'page_fc_nz_info.html', {
        'tt':   1,
    })

def page_fc_world_info(request):
    return render(request, 'page_fc_world_info.html', {
        'tt':   1,
    })

def page_fc_food_composition_db(request):
    return render(request, 'page_fc_food_composition_db.html', {
        'tt':   1,
    })


def page_fc_make_claim(request):
    return render(request, 'page_fc_make_claim.html', {
        'tt':   1,
    })


# Create your views here.
