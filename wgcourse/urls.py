import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('accounts.urls')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]

urlpatterns += [
     path('catalog/', include('catalog.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
