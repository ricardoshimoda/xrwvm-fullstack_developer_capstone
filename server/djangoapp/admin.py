from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5


class CarModelAdmin(admin.ModelAdmin):
    model = CarModel
    list_filter = ['type']
    search_fields = ['name']


class CarMakeAdmin(admin.ModelAdmin):
    model = CarMake
    inlines = [CarModelInline]


admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
