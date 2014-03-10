# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

import logging
import datetime
import inspect
import sys


##################################################################
## 
## 
##################################################################

class BdbEntry(models.Model):
    name = models.CharField(max_length=255, unique=True)
    alias = models.CharField(max_length=255, blank=True)
    descr = models.CharField(max_length=255, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_last = models.DateField(auto_now=True)
    user = models.CharField(max_length=255)
    ref = models.TextField(blank=True)    

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

class BdbUnit(BdbEntry):
    class Meta:
        db_table = 'bdb_unit'

#@receiver(pre_save, sender=BdbEntry)
#def bdb_entry_date_last(sender, instance, *args, **kwargs):
#    instance.date_last = datetime.datetime.now()
#    if(instance.date_created is None):
#        instance.date_created = datetime.datetime.now()

class BdbConfig(BdbEntry):
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_config'

class BdbFoodAttribute(BdbEntry):
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_food_attribute'


class BdbSymptom(BdbEntry):
    """ A symptom (from Greek , "accident, misfortune, that which befalls", "I befall", "together, with" , "I fall") is a departure from normal function or feeling which is noticed by a patient, indicating the presence of disease or abnormality. A symptom is subjective, observed by the patient, and cannot be measured directly
    """
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_symptom'

class BdbHealthClaim(BdbEntry):
    """ A claim on a food that the food has a certain health benefits for the consumer. A food claim can be simple like
'Contains Vitam C' or a high level claim like for instance 'This food helps perventing hard attacks' which is difficult to prove.
    """
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_food_claim'

class BdbDisease(BdbEntry):
    """ A disease is an abnormal condition that affects the body of an organism.
    """
    symp = models.ManyToManyField(BdbSymptom, blank=True)
    fcla = models.ManyToManyField(BdbHealthClaim, blank=True)
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_disease'

class BdbPathway(BdbEntry):
    """ A claim on a food that the food has a certain health benefits for the consumer. A food claim can be simple like
'Contains Vitam C' or a high level claim like for instance 'This food helps perventing hard attacks' which is difficult to prove.
    """
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_physiology'


class BdbFood(BdbEntry):
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_food'


class BdbBiomarker(BdbEntry):
    """ A biomarker, or biological marker, generally refers to a measured characteristic which may be used as an indicator of some biological state or condition. The term occasionally also refers to a substance whose presence indicates the existence of living organisms.
Biomarkers are often measured and evaluated to examine normal biological processes, pathogenic processes, or pharmacologic responses to a therapeutic intervention. Biomarkers are used in many scientific fields.
    """
    phys = models.ManyToManyField(BdbPathway, blank=True)
    dise = models.ManyToManyField(BdbDisease)
    #food = models.ManyToManyField(BdbFood, through='BdbFoodBiomarker', blank=True)
    food = models.ManyToManyField(BdbFood)
    fcla = models.ManyToManyField(BdbHealthClaim, blank=True)
    #fatt = models.ManyToManyField(BdbFoodAttribute, through='BdbFoodAttributeBiomarkerEffect', blank=True)
    fatt = models.ManyToManyField(BdbFoodAttribute)

    unit = models.ForeignKey(BdbUnit, blank=True)

    class Meta(BdbEntry.Meta):
        db_table = 'bdb_biomarker'

    def add_kv(self, k, v):
        if(v is None):
            v = "None"
        att_k, created = BdbAttribKey.objects.get_or_create(name=k)
        att,created = self.bdbattrib_set.get_or_create(attrib_key=att_k)
        att.value = v
        att.save()

    def add_kv_from_array(self, k, v):
        vs = v.split(',')
        for val in vs:
            self.add_kv(k,val)

    def add_symp_from_array(self, disease, value):
        syms = value.split(',')
        for sym in syms:
            if(sym is None or sym.strip() == ""):
                sym = "None"

            symp, created = BdbSymptom.objects.get_or_create(name=sym)
            disease.symp.add(symp)



    def add_dise_from_array(self, row):
        dss = row[7].split(',')
        for ds in dss:
            if(ds is None or ds.strip() == ""):
                ds = "None"
            dise, created = BdbDisease.objects.get_or_create(name=ds)
            dise.unit = BdbUnit.objects.get_or_create(name='None')
            self.add_symp_from_array(dise, row[8])
            dise.save()
            self.dise.add(dise)

    def add_phys_from_array(self, values):
        phs = values.split(',')
        for ph in phs:
            if(ph is None or ph.strip() == ""):
                ph = "None"
            phys, created = BdbPathway.objects.get_or_create(name=ph)
            self.phys.add(phys)

    def add_food_from_array(self, row):
        vs = row[18].split(',')
        for v in vs:
            if(v is None or v.strip() == ""):
                v = "None"
            o,created = BdbFood.objects.get_or_create(name=v)
            self.food.add(o)
            self.add_fatt_from_array(o, row[19])
            self.add_fatt_from_array(o, row[20])
            
    def add_fatt_from_array(self, food, values):
        vs = values.split(',')
        for v in vs:
            if(v is None or v.strip() == ""):
                v = "None"
            o,created = BdbFoodAttribute.objects.get_or_create(name=v)
            self.fatt.add(o)


class BdbFoodAttributeBiomarkerEffect(models.Model):
    threshhold_value = models.FloatField()
    threshhold_unit  = models.ForeignKey(BdbUnit)
    food_attribute   = models.ForeignKey(BdbFoodAttribute)
    biomarker        = models.ForeignKey(BdbBiomarker)
    class Meta:
        db_table = 'bdb_attribute_biomarker_effect'

class BdbFoodBiomarker(models.Model):
    food      = models.ForeignKey(BdbFood)
    biomarker = models.ForeignKey(BdbBiomarker)
    descr     = models.TextField(blank=True)
    sci_relia = models.TextField(blank=True)

class BdbAttribKey(BdbEntry):
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_attrib_key'

class BdbFoodAttributeValue(models.Model):
    food_attribute = models.ForeignKey(BdbFoodAttribute)
    food           = models.ForeignKey(BdbFood)
    unit           = models.ForeignKey(BdbUnit, blank=True)
    class Meta:
        db_table = 'bdb_food_attribute_value'

#pre_save.connect(bdb_entry_date_last, sender=BdbAttribKey)

class BdbAttrib(models.Model):
    attrib_key   = models.ForeignKey(BdbAttribKey)
    value = models.TextField(blank=True)

    biom  = models.ForeignKey(BdbBiomarker)
    #dise  = models.ForeignKey(BdbDisease, blank=True)
    class Meta:
        db_table = 'bdb_attrib'
    def __unicode__(self):
        return self.attrib_key.name + '/' + self.value


