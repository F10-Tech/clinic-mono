
import os
from django.db.models.signals import post_save, post_delete, pre_save
from django.core.files.storage import default_storage
from .models import *
from projct_alpha_api.settings import MEDIA_ROOT

def check_img_service(sender, instance, **kwargs):

    # find the new image if exist in storage
    new_image_light = str(instance.image_light)
    new_image_dark = str(instance.image_dark)

    old_image_light = MEDIA_ROOT + "/images/service/"+ new_image_light
    old_image_dark = MEDIA_ROOT + "/images/service/"+ new_image_dark

    if default_storage.exists(old_image_light):
        # delete the old image form storage
        default_storage.delete(old_image_light)

    if default_storage.exists(old_image_dark):
        # delete the old image form storage
        default_storage.delete(old_image_dark)

def check_img_subservice(sender, instance, **kwargs):

    # find the new image if exist in storage
    new_image_light = str(instance.image_light)
    new_image_dark = str(instance.image_dark)

    old_image_light = MEDIA_ROOT + "/images/subservice/"+ new_image_light
    old_image_dark = MEDIA_ROOT + "/images/subservice/"+ new_image_dark

    if default_storage.exists(old_image_light):
        # delete the old image form storage
        default_storage.delete(old_image_light)

    if default_storage.exists(old_image_dark):
        # delete the old image form storage
        default_storage.delete(old_image_dark)




pre_save.connect(check_img_service, sender=Service)
pre_save.connect(check_img_subservice, sender=Subservice)



