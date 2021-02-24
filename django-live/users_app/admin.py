from django.contrib import admin
# Import the models
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)

# To deploy run
# 1. pip freeze > requirements.txt
# 2. create a runtime.txt and specify the python version
# 3. create a Procfile
