from django.contrib import admin

# Register your models here.

import models

class BdbAttributeAdmin(admin.ModelAdmin):
    list_display = ('oid')
    #search_fields = ('subjectname', 'subjectspeciesname')

admin.site.register(models.BdbBiomarker)
admin.site.register(models.BdbPathway)
admin.site.register(models.BdbAttrib)
admin.site.register(models.BdbAttribKey)
admin.site.register(models.BdbDisease)
admin.site.register(models.BdbSymptom)
admin.site.register(models.BdbFood)
admin.site.register(models.BdbHealthClaim)
admin.site.register(models.BdbFoodAttribute)
admin.site.register(models.BdbConfig)


