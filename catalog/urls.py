from django.urls import path
from catalog.views import GoldViewSet, GoldImageView, PremiumImageView, PremiumViewSet, TankImageView, TankViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'gold', GoldViewSet, basename='gold')
urlpatterns = router.urls

urlpatterns += [
    path('gold/<int:gold_pk>/images/<int:gold_image_pk>/', GoldImageView.as_view(), name='gold-image')
]

urlpatterns += [
    path('premium/<int:premium_pk>/images/<int:premium_image_pk>/', PremiumImageView.as_view(), name='premium-image')
]

urlpatterns += [
    path('tanks/<int:tank_pk>/images/<int:tank_image_pk>/', TankImageView.as_view(), name='tank-image')
]
