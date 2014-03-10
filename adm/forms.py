from django.forms import ModelForm
from api.models import BdbBiomarker, BdbAttrib, BdbAttribKey

class BdbBiomarkerForm(ModelForm):
    class Meta:
        model = BdbBiomarker
        fields = ['name', 'alias', 'descr']


class BdbAttribForm(ModelForm):
    class Meta:
        model = BdbAttrib
        fields = ['value']


