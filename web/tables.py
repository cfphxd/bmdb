import django_tables2 as tables
from api.models import *

class BdbBiomarkerTable(tables.Table):
    name = tables.Column(verbose_name="Name", orderable=True)
    descr = tables.Column(orderable=False)
    class Meta:
        model = BdbBiomarker 
        attrs = {"class": "paleblue"}
        fields = ('name', 'descr')


