from rest_framework import viewsets
from rest_framework import generics

from catalog.serializers import GoldSerializer, GoldImageSerializer, PremiumSerializer, PremiumImageSerializer, \
    TankSerializer, TankImageSerializer, TypeSerializer, NationSerializer, CurrencySerializer
from catalog.models import Gold, GoldImage, Premium, PremiumImage, Tank, TankImage, TankType, TankNation, Currency


class GoldViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GoldSerializer
    queryset = Gold.objects.all()


class GoldImageView(generics.RetrieveAPIView):
    serializer_class = GoldImageSerializer

    def get_queryset(self):
        return GoldImage.objects.filter(gold__pk=self.kwargs['gold_pk'])

    def get_object(self):
        return self.get_queryset().get(pk=self.kwargs['gold_image_pk'])


class PremiumViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PremiumSerializer
    queryset = Premium.objects.all()


class PremiumImageView(generics.RetrieveAPIView):
    serializer_class = PremiumImageSerializer

    def get_queryset(self):
        return PremiumImage.objects.filter(premium__pk=self.kwargs['premium_pk'])

    def get_object(self):
        return self.get_queryset().get(pk=self.kwargs['premium_image_pk'])


class TankViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TankSerializer
    queryset = Tank.objects.all()


class TankImageView(generics.RetrieveAPIView):
    serializer_class = TankImageSerializer

    def get_queryset(self):
        return TankImage.objects.filter(tank__pk=self.kwargs['tank_pk'])

    def get_object(self):
        return self.get_queryset().get(pk=self.kwargs['tank_image_pk'])


class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TypeSerializer
    queryset = TankType.objects.all()


class NationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NationSerializer
    queryset = TankNation.objects.all()


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.filter(is_active=True)
