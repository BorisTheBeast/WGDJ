from django.urls import reverse
from rest_framework import serializers

from catalog.models import ProdType, ProdImage, AllProducts, Gold, GoldImage, Premium, PremiumImage, TankImage, Tank, TankType, TankNation, Currency


class GoldImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GoldImage
        fields = ['id', 'image']


class GoldSerializer(serializers.ModelSerializer):
    images = GoldImageSerializer('gold-image', many=True, required=False)

    class Meta:
        model = Gold
        fields = ['id', 'uuid', 'title', 'description', 'main_image', 'price', 'promo', 'discount', 'images', 'display', 'priority']

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


class PremiumImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PremiumImage
        fields = ['id', 'image']


class PremiumSerializer(serializers.ModelSerializer):
    images = PremiumImageSerializer('premium-image', many=True, required=False)

    class Meta:
        model = Premium
        fields = ['id', 'uuid', 'title', 'description', 'main_image', 'price', 'promo', 'discount', 'images', 'display', 'priority']

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


class TankImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TankImage
        fields = ['id', 'image']


class TankNationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TankNation
        fields = ['name', 'icon']


class TankTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TankType
        fields = ['name', 'icon']


class TankSerializer(serializers.ModelSerializer):
    images = TankImageSerializer('tank-image', many=True, required=False)
    nation = TankNationSerializer(read_only=True)
    type = TankTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Tank
        fields = ['id', 'uuid', 'title', 'description', 'main_image', 'price', 'promo', 'discount', 'images', 'display', 'type', 'nation',
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
        fields = ['name', 'icon']


class NationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TankNation
        fields = ['name', 'icon']


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['name', 'is_active']


class ProdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdType
        fields = ['name']


class ProdImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProdImage
        fields = ['image']


class AllProdSerializer(serializers.ModelSerializer):
    prod_type = ProdTypeSerializer(many=True, read_only=True)
    images = ProdImageSerializer('prod-image', many=True, required=False)
    nation = TankNationSerializer(read_only=True)
    type = TankTypeSerializer(many=True, read_only=True)

    class Meta:
        model = AllProducts
        fields = ['prod_type', 'id', 'uuid', 'title', 'description', 'main_image', 'price', 'promo', 'discount',
                  'images', 'display', 'type', 'nation', 'priority', 'tier']

    def create(self, validated_data):
        if 'images' in validated_data:
            images = validated_data.pop('images')
        else:
            images = []

        obj = AllProducts.objects.create(**validated_data)

        for data in images:
            data['all'] = obj
            ProdImage.objects.create(**data)

        return obj
