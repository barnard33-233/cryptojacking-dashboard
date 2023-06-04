from django.test import TestCase
from django.shortcuts import render
from django.db import models
from django.http import HttpRequest, HttpResponse,JsonResponse
from django.core import serializers
from .models import DeviceRecord, Modified
from .apps import mtime
import json

test_data = []

# Create your tests here.

# test ajax.
def response_AjaxTest(request: HttpRequest):
    devices = [
        DeviceRecord(mac="ff:ff:ff:ff:ff:ff", ip="255.255.255.255", safety=1),
        DeviceRecord(mac="00:00:00:00:00:00", ip="0.0.0.0", safety=0),
    ]
    devices_json = {}
    devices_json['data'] = json.loads(serializers.serialize('json', devices))
    response = JsonResponse(devices_json)
    return response
