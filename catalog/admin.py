from django.contrib import admin
from .models import Gold, GoldImage, Premium, PremiumImage


class GoldImageInline(admin.TabularInline):
    model = GoldImage


@admin.register(Gold)
class GoldAdmin(admin.ModelAdmin):
    inlines = [GoldImageInline]


class PremiumImageInline(admin.TabularInline):
    model = PremiumImage


@admin.register(Premium)
class PremiumAdmin(admin.ModelAdmin):
    inlines = [PremiumImageInline]
