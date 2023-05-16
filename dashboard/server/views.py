from django.shortcuts import render
from django.db import models
from django.http import HttpRequest, HttpResponse,JsonResponse
from django.core import serializers
from .models import mtime, DeviceRecord, Modified
import json

# Create your views here.

device_record: models.QuerySet

def response_DeviceRecord(request: HttpRequest):
    global device_record
    new_mtime = Modified.objects.all()[0].mtime
    if new_mtime != mtime:
        device_record = DeviceRecord.objects.all()
    device_record_json = {}
    device_record_json['data'] = json.loads(serializers.serialize('json', device_record))
    return JsonResponse(device_record_json)

def response_AjaxTest(request: HttpRequest):
    devices = [
        DeviceRecord(mac="ff:ff:ff:ff:ff:ff", ip="255.255.255.255", safety=1),
        DeviceRecord(mac="00:00:00:00:00:00", ip="0.0.0.0", safety=0),
    ]
    devices_json = {}
    devices_json['data'] = json.loads(serializers.serialize('json', devices))
    response = JsonResponse(devices_json)
    return response