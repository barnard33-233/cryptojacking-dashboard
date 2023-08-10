from django.shortcuts import render
from django.db import models
from django.http import HttpRequest, HttpResponse,JsonResponse
from django.core import serializers
from .models import DeviceRecord, Modified
import json

from django.core.exceptions import ObjectDoesNotExist
import datetime
import threading
import classifier.classify as classify

mtime = ""


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
        while True:
            print("[+] Classify Start")

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


# start detector
detector = Detector()
detector_thread = threading.Thread(target = detector.mainloop)
detector_thread.start()


print("[D] im running.")

device_record: models.QuerySet

def response_DeviceRecord(request: HttpRequest):
    global device_record
    global mtime
    new_mtime = Modified.objects.all()[0].mtime
    if new_mtime != mtime:
        print("Record Updated")
        device_record = DeviceRecord.objects.all()
        mtime = new_mtime
    device_record_json = {}
    device_record_json['data'] = json.loads(serializers.serialize('json', device_record))
    return JsonResponse(device_record_json)
