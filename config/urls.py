from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from innovar.views import (
    UsuarioCustomizadoViewSet,
    ProcedimentoViewSet,
    PacoteViewSet,
    ClienteProcedimentoViewSet,
    ClientePacoteViewSet
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

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
