import os
import random
from django.db import models


def getNameAndExt(filename):
    basename = os.path.basename(filename)
    name, ext = os.path.splitext(basename)
    return name, ext


def image_upload(instance, filename):
    name, ext = getNameAndExt(filename)
    middleName = random.randint(1, 1000000)
    newName = "{name}{middleName}".format(name=name, middleName=middleName)
    return "files/{name}/{type}/{filename}{ext}".format(
        name=instance.name,
        type=instance.type,
        filename=newName,
        ext=ext
    )


class UploadFileModel(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=5)
    file = models.FileField(upload_to=image_upload)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploaded = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
