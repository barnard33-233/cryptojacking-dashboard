from django.apps import AppConfig
from django.apps import apps
import datetime
import threading
import time
from .tests import test_data
# from .models import DeviceRecord, Modified
mtime = ""

class ServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server'

    def ready(self) -> None:
        global mtime
        mtime = ""
        DeviceRecord = apps.get_model('server', 'devicerecord')
        Modified = apps.get_model('server', 'modified')
        Modified_count = Modified.objects.count()
        print(Modified_count)
        if Modified_count == 0:
            Modified.objects.create(mtime=datetime.datetime.now())
        elif Modified_count > 1:
            Modified.objects.all().delete()
            Modified.objects.create(mtime=datetime.datetime.now())
        else:
            Modified.objects.all().update(mtime=datetime.datetime.now())
        print(Modified.objects.count())
        # start detector subprocess

        start_detector()

        print("Server started.")

        return super().ready()


# TODO: All things below
class Detector:
    def __init__(self) -> None:
        # TODO call the real init function here
        pass

    def packet_capture(self):
        # TODO call the real packet_capture here
        return None
    
    def classify(self, data):
        # call the real classifier here
        return None

    def mainloop(self):
        while True:
            print("mainloop running")
            time.sleep(3) # XXX DEBUG, delete this later

            # get data
            data = self.packet_capture()

            # classify
            result = self.classify(data)

            # write it to database
            # TODO


def start_detector():
    # new a Detector
    detector = Detector()
    # create a subprocess
    detector_thread = threading.Thread(target=detector.mainloop)
    detector_thread.start()
    pass
