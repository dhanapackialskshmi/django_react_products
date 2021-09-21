from django.contrib import admin
from api.models import Basetable, Properties,Images, Dimensions


# Register your models here.
admin.site.register(Basetable)
admin.site.register(Properties)
admin.site.register(Dimensions)
admin.site.register(Images)
