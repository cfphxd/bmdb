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


class BdbEntry(models.Model):
    name = models.CharField(max_length=255, unique=True)
    alias = models.CharField(max_length=255, blank=True)
    descr = models.CharField(max_length=255, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_last = models.DateField(auto_now=True)
    user = models.CharField(max_length=255)
    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

@receiver(pre_save, sender=BdbEntry)
def bdb_entry_date_last(sender, instance, *args, **kwargs):
    instance.date_last = datetime.datetime.now()
    if(instance.date_created is None):
        instance.date_created = datetime.datetime.now()

class BdbAttribKey(BdbEntry):
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_attrib_key'

pre_save.connect(bdb_entry_date_last, sender=BdbAttribKey)

class BdbAttrib(models.Model):
    attrib_key   = models.ForeignKey(BdbAttribKey)
    value = models.TextField(blank=True)
    class Meta:
        db_table = 'bdb_attrib'
    def __unicode__(self):
        return self.attrib_key.name + '/' + self.value

class BdbConfig(BdbEntry):
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_config'

class BdbDisease(BdbEntry):
    """ A disease is an abnormal condition that affects the body of an organism.
    """
    att = models.ManyToManyField(BdbAttrib)
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_disease'

class BdbFood(BdbEntry):
    att = models.ManyToManyField(BdbAttrib)
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_food'

class BdbFoodAttribute(BdbEntry):
    att = models.ManyToManyField(BdbAttrib)
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_food_attribute'


class BdbFoodComponent(BdbEntry):
    att = models.ManyToManyField(BdbAttrib)
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_food_component'

class BdbSymptom(BdbEntry):
    """ A symptom (from Greek , "accident, misfortune, that which befalls", "I befall", "together, with" , "I fall") is a departure from normal function or feeling which is noticed by a patient, indicating the presence of disease or abnormality. A symptom is subjective, observed by the patient, and cannot be measured directly
    """
    att = models.ManyToManyField(BdbAttrib)
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_symptom'

class BdbFoodClaim(BdbEntry):
    """ A claim on a food that the food has a certain health benefits for the consumer. A food claim can be simple like
'Contains Vitam C' or a high level claim like for instance 'This food helps perventing hard attacks' which is difficult to prove.
    """
    att = models.ManyToManyField(BdbAttrib)
    class Meta(BdbEntry.Meta):
        db_table = 'bdb_food_claim'

class BdbBiomarker(BdbEntry):
    """ A biomarker, or biological marker, generally refers to a measured characteristic which may be used as an indicator of some biological state or condition. The term occasionally also refers to a substance whose presence indicates the existence of living organisms.
Biomarkers are often measured and evaluated to examine normal biological processes, pathogenic processes, or pharmacologic responses to a therapeutic intervention. Biomarkers are used in many scientific fields.
    """
    att  = models.ManyToManyField(BdbAttrib)
    dise = models.ManyToManyField(BdbDisease)
    food = models.ManyToManyField(BdbFood)
    symp = models.ManyToManyField(BdbSymptom)
    fcom = models.ManyToManyField(BdbFoodComponent)
    fcla = models.ManyToManyField(BdbFoodClaim)

    class Meta(BdbEntry.Meta):
        db_table = 'bdb_biomarker'


