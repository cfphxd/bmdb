from api.models import BdbAttrib, BdbAttribKey, BdbBiomarker, BdbDisease, BdbFood, BdbFoodComponent, BdbSymptom, BdbConfig
from django.db.utils import IntegrityError, DatabaseError

def run():

    key, created = BdbAttribKey.objects.get_or_create(name='Headache2')
    sym, created = BdbSymptom.objects.get_or_create(name='Symp3')
    BdbAttrib.objects.filter(attrib_key__name='Headache2', bdbsymptom__id=sym.id).delete()
    att = BdbAttrib(attrib_key=key, value='test2') 
    att.save()
    sym.att.add(att)
    print BdbAttrib.objects.filter(attrib_key__name='Headache2', bdbsymptom__id=sym.id) 


