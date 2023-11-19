from django.contrib import admin
from .models import Conf_hall

@admin.register(Conf_hall)
class Conf_hallAdmin(admin.ModelAdmin):
	
	list_display = ['hall_name']





