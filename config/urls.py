from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from innovar.views import (
    ProcedimentoViewSet,
    PacoteViewSet,
    HorarioBloqueadoViewSet,

  
)
from uploader.views import (
    ImageUploadViewSet,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = DefaultRouter()

router.register(r'procedimentos', ProcedimentoViewSet)
router.register(r'pacotes', PacoteViewSet)
router.register(r'imagens', ImageUploadViewSet)
router.register(r'horarios_bloqueados', HorarioBloqueadoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/", include(router.urls)),

]


urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
