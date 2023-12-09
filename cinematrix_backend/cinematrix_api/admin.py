from django.contrib import admin
from cinematrix_api.models import *

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(StreamingSite)
admin.site.register(Language)

# Register your models here.
