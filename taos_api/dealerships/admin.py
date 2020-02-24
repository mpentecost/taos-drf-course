from django.contrib import admin

from .models import Dealership, Auto, Sale


@admin.register(Dealership)
class DealershipAdmin(admin.ModelAdmin):
    pass


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    pass


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass
