from meta_manager.models import PFR_Meta
from django.db.models import Q


class MetaManager:

    def Purge(self):
        PFR_Meta.objects.all().delete()

    def GetMeta(self, meta_key, meta_value):
        return PFR_Meta.objects.filter(Q(meta_key=meta_key) | Q(meta_value=meta_value))

    def RemoveMeta(self, meta_key, meta_value):
        self.GetMeta(meta_key, meta_value).delete()

    def AddMeta(self, meta_key, meta_value):
        if(self.GetMeta(meta_key, meta_value)):
            return True
        else:
            m = PFR_Meta(meta_key=meta_key,meta_value=meta_value)
            m.save()

    def PurgeKey(self, meta_key):
        PFR_Meta.objects.filter(meta_key=meta_key).delete()

    def GetKey(self, meta_key):
        return PFR_Meta.objects.filter(meta_key=meta_key)



