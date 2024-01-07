
import os
from django.db.models.signals import post_save, post_delete, pre_save
from django.core.files.storage import default_storage
from .models import *
from projct_alpha_api.settings import MEDIA_ROOT

def check_img_patient(sender, instance, **kwargs):

    # find the new image if exist in storage
    new_image_1 = str(instance.img_1)
    new_image_2 = str(instance.img_2)

    print(new_image_1)

    old_image_1 = MEDIA_ROOT + "/images/"+ new_image_1
    old_image_2 = MEDIA_ROOT + "/images/"+ new_image_2

    if default_storage.exists(old_image_1):
        # delete the old image form storage
        default_storage.delete(old_image_1)

    if default_storage.exists(old_image_2):
        # delete the old image form storage
        default_storage.delete(old_image_2)






pre_save.connect(check_img_patient, sender=Patient)



