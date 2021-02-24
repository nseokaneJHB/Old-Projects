# For receivers
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User, Group
from .models import Customer


# Responsible for creating a customer profile
# @receiver(post_save, sender=User)
def customer_profile(sender, instance, created, **kwargs):
    if created:
        # Associated a user to customer automatically
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        Customer.objects.create(
            user=instance,
            name=instance.username,
        )
        print('Profile created')


# Save that customer
post_save.connect(customer_profile, sender=User)

# 1. Configure this in the apps.py
#       def ready(self):
#           import users_app.signals
#
# 2. pass app_name.app.signal_name in settings.py
#
# OR
#
# 2. pass default_app_config = 'app_name.apps.config_file_name'
