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
        try:
            DeviceRecord = apps.get_model('server', 'devicerecord')
            Modified = apps.get_model('server', 'modified')
        except Exception as e:
            # if database is not prepared, do migration
            print("[!] This should be a migration!")
            print(e)
            # TODO: report
            return super().ready()

        
        Modified_count = Modified.objects.count()
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
        start_detector()
        print("[+] Server started...")

        return super().ready()


class Detector:
    def __init__(self) -> None:
        self.df = classify.init()
        pass

    def packet_capture(self):
        # TODO call the real packet_capture here
        return None
    
    def classify(self, data):
        return classify.classifier(self.df)

    def mainloop(self):
        DeviceRecord = apps.get_model('server', 'devicerecord')
        Modified = apps.get_model('server', 'modified')
        while True:
            print("[+] Classify Start")
            # time.sleep(3) # XXX DEBUG, delete this later

            # get data
            data = self.packet_capture()

            # classify
            results = self.classify(data)
            # write it to database
            for result in results:
                data = result['data']
                try:
                    record = DeviceRecord.objects.get(mac=result['mac'])
                except ObjectDoesNotExist:
                    record = DeviceRecord.objects.create(mac=result['mac'], ip=data['ip'], safety=data['safety'])
                else:
                    record.ip = data['ip']
                    record.safety = data['safety']
                    record.save()
            Modified.objects.all().update(mtime=datetime.datetime.now())
            print("[+] Classify end")


def start_detector():
    # new a Detector
    detector = Detector()
    # create a subprocess
    detector_thread = threading.Thread(target=detector.mainloop)
    detector_thread.start()
    pass
