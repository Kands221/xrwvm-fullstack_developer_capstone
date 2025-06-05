from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class for inline display in CarMakeAdmin
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 3

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'car_type', 'year', 'dealer_id')
    search_fields = ['name', 'car_make__name']
    list_filter = ('car_type', 'car_make')

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name']
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
