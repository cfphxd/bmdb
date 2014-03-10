import django_tables2 as tables
from api.models import *

class BdbBiomarkerTable(tables.Table):
    name = tables.Column(verbose_name="Name", orderable=True)
    descr = tables.Column(orderable=False)
    att = tables.Column()
    class Meta:
        model = BdbBiomarker 
        attrs = {"class": "paleblue"}
        fields = ('name', 'descr', 'att')

class BdbAttribTable(tables.Table):
    biomarker = tables.Column(accessor='bdbbiomarker.name')
    class Meta:
        model = BdbAttrib
        attrs = {"class": "paleblue"}
        fields = ('attrib_key', 'value')


