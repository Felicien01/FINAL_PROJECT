from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

class CarModelInLine(admin.StackedInline) :
    model = CarModel
    extra = 5
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['name', 'dealer', 'Type', 'year']
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [CarModelInLine]
# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)