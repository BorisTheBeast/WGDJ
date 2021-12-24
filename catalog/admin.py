from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import ProdImage, AllProducts, GoldImage, Premium, PremiumImage, Tank, TankImage, TankType, TankNation, \
    Currency, Gold, ProdType
from django.contrib import messages


# class GoldImageInline(admin.TabularInline):
#     model = GoldImage


# @admin.register(Gold)
# class GoldAdmin(SortableAdminMixin, admin.ModelAdmin):
#     inlines = [GoldImageInline]
#     list_display = ['title', 'id', 'price', 'promo', 'discount', 'display', 'priority', 'sort_order']
#     list_filter = ['display', 'promo', 'priority', 'price']
#     search_fields = ['title']
#     readonly_fields = ['sort_order']


# class PremiumImageInline(admin.TabularInline):
#     model = PremiumImage


# @admin.register(Premium)
# class PremiumAdmin(SortableAdminMixin, admin.ModelAdmin):
#     inlines = [PremiumImageInline]
#     list_display = ['title', 'id', 'price', 'promo', 'discount', 'display', 'priority', 'sort_order']
#     list_filter = ['display', 'promo', 'priority', 'price']
#     search_fields = ['title']
#     readonly_fields = ['sort_order']


# class TankImageInline(admin.TabularInline):
#     model = TankImage


# @admin.register(Tank)
# class TankAdmin(SortableAdminMixin, admin.ModelAdmin):
#     inlines = [TankImageInline]
#     list_display = ['title', 'id', 'nation', 'tier', 'price', 'promo', 'discount', 'display', 'priority', 'sort_order']
#     list_filter = ['display', 'nation', 'promo', 'priority']
#     search_fields = ['title', 'nation__name']
#     readonly_fields = ['sort_order']
#     filter_horizontal = ['type']


@admin.register(TankType)
class TankTypeAdmin(admin.ModelAdmin):
    model = TankType


@admin.register(TankNation)
class TankNationAdmin(admin.ModelAdmin):
    model = TankNation


admin.action(description='Mark selected currency active')
def make_active(modeladmin, request, queryset):
    if queryset.count() == 1:
        Currency.objects.filter(is_active=True).update(is_active=False)
        queryset.update(is_active=True)
        row = queryset.first()
        messages.add_message(request, messages.SUCCESS, f'{row.name} set as active currency for store')
    else:
        messages.add_message(request, messages.ERROR, 'You should select one currency row to make it active')


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    readonly_fields = ['is_active']
    list_display = ['name', 'is_active']
    actions = [make_active]


class ProdImageInline(admin.TabularInline):
    model = ProdImage


@admin.register(ProdType)
class ProdTypeAdmin(admin.ModelAdmin):
    model = ProdType


admin.action(description='Mark selected items to show')
def show_items(modeladmin, request, queryset):
    queryset.update(display=True)
    row = queryset.first()
    messages.add_message(request, messages.SUCCESS, f'set as displayed items for store')


admin.action(description='Mark selected items to show')
def hide_items(modeladmin, request, queryset):
    queryset.update(display=False)
    row = queryset.first()
    messages.add_message(request, messages.SUCCESS, f'set as displayed items for store')


@admin.register(AllProducts)
class AllProductsAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ProdImageInline]
    list_display = ['title', 'id', 'nation', 'tier', 'price', 'promo', 'discount', 'display', 'priority', 'sort_order']
    list_filter = ['display', 'nation', 'promo', 'priority', 'prod_type']
    search_fields = ['title', 'nation__name']
    readonly_fields = ['sort_order']
    filter_horizontal = ['type']
    actions = [show_items, hide_items]
