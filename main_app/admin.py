from django.contrib import admin
# Import your models here.
from .models import Game, Playing

# Register your models here.
admin.site.register(Game)
admin.site.register(Playing)