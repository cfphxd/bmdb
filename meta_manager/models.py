from django.db import models

# Create your models here.

class PFR_Meta(models.Model):
    meta_key   = models.CharField(max_length=40, db_index=True)
    meta_value = models.TextField(default=None, db_index=True)

    def __unicode__(self):
        return self.meta_key + "/" + self.meta_value

    class Meta:
        db_table = 'pfr_meta'

		

