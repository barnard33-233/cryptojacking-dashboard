from django.apps import AppConfig
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
import datetime
import threading
import classifier.classify as classify
mtime = ""

class ServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server'

    def ready(self) -> None:
        # TODO: try catch
        global mtime
        mtime = ""
        DeviceRecord = apps.get_model('server', 'devicerecord')
        Modified = apps.get_model('server', 'modified')

        try:        
            Modified_count = Modified.objects.count()
        except Exception as e:
            # if database is not prepared, do migration
            print("[!] This should be a migration!")
            print(e)
            # TODO: report
            return super().ready()

        print(Modified_count)
        if Modified_count == 0:
            Modified.objects.create(mtime=datetime.datetime.now())
        elif Modified_count > 1:
            Modified.objects.all().delete()
            Modified.objects.create(mtime=datetime.datetime.now())
        else:
            Modified.objects.all().update(mtime=datetime.datetime.now())

        # delete all device record
        DeviceRecord.objects.all().delete()
        print(Modified.objects.count())

        # start detector subprocess

        return super().ready()

