from django.contrib import admin
from .models import *

# admin.site.register(BaseModelMixin)
admin.site.register(UserAuthentication)
admin.site.register(AppBaseConfig)
admin.site.register(UserCredentialValidation)
