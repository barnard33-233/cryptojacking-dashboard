from django.db import models

mtime = ""


class DeviceRecord(models.Model):

    class SafetyChoise(models.IntegerChoices):
        SAFE = 0, 'SAFE'
        DANGEROUS = 1, 'DANGEROUS'

    mac = models.CharField(
        max_length=17,
        primary_key=True
    ) # xx:xx:xx:xx:xx:xx

    ip = models.CharField(max_length=15)  # xxx.xxx.xxx.xxx

    safety = models.IntegerField(
        default=SafetyChoise.SAFE,
        choices=SafetyChoise.choices
    )

    time = models.DateTimeField(auto_now=True)

class Modified(models.Model):
    mtime = models.DateTimeField()