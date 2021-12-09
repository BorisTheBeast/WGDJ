from django.urls import path
from catalog.views import GoldViewSet, GoldImageView, PremiumImageView, PremiumViewSet, TankImageView, TankViewSet, TypeViewSet, NationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'gold', GoldViewSet, basename='gold')
router.register(r'premium', PremiumViewSet, basename='premium')
router.register(r'tanks', TankViewSet, basename='tanks')
router.register(r'type', TypeViewSet, basename='type')
router.register(r'nation', NationViewSet, basename='nation')
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
