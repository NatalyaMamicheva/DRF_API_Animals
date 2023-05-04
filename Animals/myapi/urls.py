from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(views.AnimalsAPIView)
router.register(views.TypeAPIView)
router.register(views.AnimalsAPIUpdate)
router.register(views.AnimalsAPIDetailView)
router.register(views.AnimalsAPIList)
router.register(views.TypeAPIList)
router.register(views.TypeAPIUpdate)
router.register(views.TypeAPIDetailView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework'))
]
