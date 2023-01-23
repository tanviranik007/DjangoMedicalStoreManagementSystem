# import ..., include

from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from DjangoMedicalApp import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router=routers.DefaultRouter()
router.register("company",views.CompanyViewSet, basename="company")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/gettoken/',TokenObtainPairView.as_view(),name="gettoken"),
    path('api/resfresh_token/',TokenRefreshView.as_view(),name="refresh_token"),
]
