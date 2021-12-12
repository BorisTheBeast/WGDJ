from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Gold, GoldImage, Premium, PremiumImage, Tank, TankImage,TankType, TankNation, ExchangeCurrency, \
    Currency


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
class TankAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [TankImageInline]
    list_display = ['title', 'id', 'nation', 'tier', 'price', 'promo', 'discount', 'display', 'priority', 'sort_order']
    list_filter = ['display', 'nation', 'promo', 'priority']
    search_fields = ['title', 'nation__name']
    readonly_fields = ['sort_order']
    filter_horizontal = ['type']


@admin.register(TankType)
class TankTypeAdmin(admin.ModelAdmin):
    model = TankType


@admin.register(TankNation)
class TankNationAdmin(admin.ModelAdmin):
    model = TankNation


@admin.register(ExchangeCurrency)
class ExchangeCurrencyAdmin(admin.ModelAdmin):
    model = ExchangeCurrency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    model = Currency
