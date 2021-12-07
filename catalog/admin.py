from django.contrib import admin
from .models import Gold, GoldImage


class GoldImageInline(admin.TabularInline):
    model = GoldImage


@admin.register(Gold)
class GoldAdmin(admin.ModelAdmin):
    inlines = [GoldImageInline]
    