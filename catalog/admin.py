from django.contrib import admin
from .models import Gold, GoldImage, Premium, PremiumImage, Tank, TankImage,TankType, TankNation


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


class TankImageInline(admin.TabularInline):
    model = TankImage


@admin.register(Tank)
class TankAdmin(admin.ModelAdmin):
    inlines = [TankImageInline]


@admin.register(TankType)
class TankTypeAdmin(admin.ModelAdmin):
    model = TankType


@admin.register(TankNation)
class TankNationAdmin(admin.ModelAdmin):
    model = TankNation
