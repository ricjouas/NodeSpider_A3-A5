from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'temperature', views.TempViewSet)
router.register(r'humidity', views.HumidViewSet)
router.register(r'motion', views.MotionViewSet)

# Auto URL Routing for API
# login URL set
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]