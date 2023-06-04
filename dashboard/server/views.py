from django.shortcuts import render
from django.db import models
from django.http import HttpRequest, HttpResponse,JsonResponse
from django.core import serializers
from .models import DeviceRecord, Modified
from .apps import mtime
import json


# Create your views here.

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

