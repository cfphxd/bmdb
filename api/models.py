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

class BdbAttrib(models.Model):
    oid = models.IntegerField(primary_key=True)
    kid = models.ForeignKey('BdbAttribKey', db_column='kid')
    value = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'bdb_attrib'

class BdbAttribKey(models.Model):
    oid = models.IntegerField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True)
    descr = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'bdb_attrib_key'

class BdbConfig(models.Model):
    oid = models.IntegerField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True)
    descr = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'bdb_config'

class BdbDisease(models.Model):
    oid = models.IntegerField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True)
    descr = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'bdb_disease'

class BdbFood(models.Model):
    oid = models.IntegerField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True)
    descr = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'bdb_food'

class BdbOb(models.Model):
    oid = models.IntegerField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True)
    descr = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'bdb_ob'

class BdbSymtpom(models.Model):
    oid = models.IntegerField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True)
    descr = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'bdb_symtpom'

