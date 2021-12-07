from rest_framework import viewsets
from rest_framework import generics

from catalog.serializers import GoldSerializer, GoldImageSerializer
from catalog.models import Gold, GoldImage


class GoldViewSet(viewsets.ModelViewSet):
    serializer_class = GoldSerializer
    queryset = Gold.objects.all()


class GoldImageView(generics.RetrieveUpdateAPIView):
    serializer_class = GoldImageSerializer

    def get_queryset(self):
        return GoldImage.objects.filter(gold__pk=self.kwargs['gold_pk'])

    def get_object(self):
        return self.get_queryset().get(pk=self.kwargs['gold_image_pk'])
