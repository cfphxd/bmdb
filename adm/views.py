from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

from api.models import BdbBiomarker, BdbAttrib, BdbAttribKey
from forms import BdbBiomarkerForm

# Create your views here.

def sequencial_data_input(request):
    biom = BdbBiomarker.objects.get(name='tt')
    #att = BdbAttrib.objects.get(id=1)
    form = BdbBiomarkerForm(instance=biom)
    #form = BdbAttribForm(instance=att)
    return render(request, 'seq_input.html', {
        'form': form,
    })


