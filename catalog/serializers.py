from django.urls import reverse
from rest_framework import serializers

from catalog.models import Gold, GoldImage, Premium, PremiumImage, TankImage, Tank, TankType, TankNation, Currency


class GoldImageHyperlinkedField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'gold_pk': obj.gold.pk,
            'gold_image_pk': obj.pk
        }
        return request.build_absolute_uri(reverse(view_name, kwargs=url_kwargs))


class GoldImageSerializer(serializers.HyperlinkedModelSerializer):
    edit_url = GoldImageHyperlinkedField(view_name='gold-image')

    class Meta:
        model = GoldImage
        fields = ['id', 'image', 'edit_url']


class GoldSerializer(serializers.ModelSerializer):
    images = GoldImageSerializer('gold-image', many=True, required=False)

    class Meta:
        model = Gold
        fields = ['id', 'uuid', 'title', 'description', 'price', 'promo', 'discount', 'images', 'display', 'priority']

    def create(self, validated_data):
        if 'images' in validated_data:
            images = validated_data.pop('images')
        else:
            images = []

        obj = Gold.objects.create(**validated_data)

        for data in images:
            data['gold'] = obj
            GoldImage.objects.create(**data)

        return obj


class PremiumImageHyperlinkedField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'premium_pk': obj.premium.pk,
            'premium_image_pk': obj.pk
        }
        return request.build_absolute_uri(reverse(view_name, kwargs=url_kwargs))


class PremiumImageSerializer(serializers.HyperlinkedModelSerializer):
    edit_url = PremiumImageHyperlinkedField(view_name='premium-image')

    class Meta:
        model = PremiumImage
        fields = ['id', 'image', 'edit_url']


class PremiumSerializer(serializers.ModelSerializer):
    images = PremiumImageSerializer('premium-image', many=True, required=False)

    class Meta:
        model = Premium
        fields = ['id', 'uuid', 'title', 'description', 'price', 'promo', 'discount', 'images', 'display', 'priority']

    def create(self, validated_data):
        if 'images' in validated_data:
            images = validated_data.pop('images')
        else:
            images = []

        obj = Premium.objects.create(**validated_data)

        for data in images:
            data['premium'] = obj
            PremiumImage.objects.create(**data)

        return obj


class TankImageHyperlinkedField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'tank_pk': obj.tank.pk,
            'tank_image_pk': obj.pk
        }
        return request.build_absolute_uri(reverse(view_name, kwargs=url_kwargs))


class TankImageSerializer(serializers.HyperlinkedModelSerializer):
    edit_url = TankImageHyperlinkedField(view_name='tank-image')

    class Meta:
        model = TankImage
        fields = ['id', 'image', 'edit_url']


class FKNameField(serializers.Field):
    def to_representation(self, value):
        return value.name


class TankTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TankType
        fields = ['id', 'name']


class TankSerializer(serializers.ModelSerializer):
    images = TankImageSerializer('tank-image', many=True, required=False)
    nation = FKNameField()
    type = TankTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Tank
        fields = ['id', 'uuid', 'title', 'description', 'price', 'promo', 'discount', 'images', 'display', 'type', 'nation',
                  'priority', 'tier']

    def create(self, validated_data):
        if 'images' in validated_data:
            images = validated_data.pop('images')
        else:
            images = []

        obj = Tank.objects.create(**validated_data)

        for data in images:
            data['tank'] = obj
            TankImage.objects.create(**data)

        return obj


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TankType
        fields = ['name']


class NationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TankNation
        fields = ['name']


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['name', 'is_active']
