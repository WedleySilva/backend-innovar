from django.urls import path, include
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from uploader.router import router as uploader_router
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from innovar.views import (
    UsuarioCustomizadoViewSet,
    ProcedimentoViewSet,
    PacoteViewSet,
    ClienteProcedimentoViewSet,
    ClientePacoteViewSet,
    HorarioBloqueadoViewSet,
    CustomTokenObtainPairView,
  
)
from uploader.views import (
    ImageUploadViewSet,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register(r'usuarios', UsuarioCustomizadoViewSet)
router.register(r'procedimentos', ProcedimentoViewSet)
router.register(r'pacotes', PacoteViewSet)
router.register(r'clientes_procedimentos', ClienteProcedimentoViewSet)
router.register(r'clientes_pacotes', ClientePacoteViewSet)
router.register(r' imagens', ImageUploadViewSet)
router.register(r'horarios_bloqueados', HorarioBloqueadoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path("api/media/", include(uploader_router.urls)),
]

path("api/media/", include(uploader_router.urls)),

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
