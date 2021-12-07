from django.urls import path
from catalog.views import GoldViewSet, GoldImageView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'gold', GoldViewSet, basename='gold')
urlpatterns = router.urls

urlpatterns += [
    path('gold/<int:gold_pk>/images/<int:gold_image_pk>/', GoldImageView.as_view(), name='gold-image')
]
