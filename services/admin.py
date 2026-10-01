from django.contrib import admin
from .models import Service, Order


# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'base_price', 'discount', 'final_price', 'is_active', 'author', 'created_at')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'description')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'client_name', 'phone', 'created_at')
    search_fields = ('client_name', 'phone', 'comment')