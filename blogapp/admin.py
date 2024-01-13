from django.contrib import admin
from .models import *
# admin.site.register(Blog)
# admin.site.register(Event)
# admin.site.register(News)
# admin.site.register(Category)

admin.site.register([Blog,Event,Category,News, Message])

# Register your models here.