# from api.models import BdbAttrib, BdbAttribKey, BdbBiomarker, BdbDisease, BdbFood, BdbFoodComponent, BdbSymptom, BdbPhysiology, BdbConfig
from api.models import *
from django.db.utils import IntegrityError, DatabaseError

import csv
from numpy import loadtxt

def add_from_array(k, biom, value):
    vs = value.split(',')
    for v in vs:
        biom.add_kv(k,v)


def run():
    with open('biomarker.csv', 'rb') as csvfile:
        biomarkers = csv.reader(csvfile)
        head = biomarkers.next()
        unit, created = BdbUnit.objects.get_or_create(name='None')
        for row in biomarkers:
            if(row[0] is None or row[0].strip() == ''):
                continue
            biom,created = BdbBiomarker.objects.get_or_create(name=row[0], unit=unit)
            biom.alias = row[2]
            biom.unit = unit
            biom.add_kv('Source tissue', row[4])
            biom.add_kv('Genetics of Biomarker', row[5])
            biom.add_kv_from_array('Type1', row[6])
            biom.add_dise_from_array(row)
            biom.add_kv('Type2', row[9])
            biom.add_phys_from_array(row[10])
            biom.add_kv('Measurement techniques', row[11])
            biom.add_kv('Companies', row[12])
            biom.add_kv('Official method', row[13])
            biom.add_kv('Review of biomarker', row[14])
            biom.add_kv('Evaluation', row[15])
            biom.add_kv('Numerical rating',row[16])
            biom.add_kv('Jurisdictions', row[17])
            biom.add_food_from_array(row)
            biom.add_kv('Literature references', row[21])
            biom.add_kv('Website', row[22])
            biom.user = row[23]
            biom.add_kv('Gender issues', row[24])
            biom.add_kv('Development stage issues', row[25])
            biom.add_kv('False positives', row[26])
            biom.add_kv('False negatives', row[27])
            biom.save()

