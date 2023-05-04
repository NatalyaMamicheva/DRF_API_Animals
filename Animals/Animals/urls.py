from django.contrib import admin
from django.urls import path, include
from myapi.views import AnimalsAPIView, TypeAPIView, AnimalsAPIUpdate, \
    AnimalsAPIDetailView, AnimalsAPIList, TypeAPIList, TypeAPIUpdate, \
    TypeAPIDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/animals/', AnimalsAPIView.as_view()),
    path('api/type/', TypeAPIView.as_view()),
    path('api/typelist/', TypeAPIList.as_view()),
    path('api/type/<int:pk>/', TypeAPIUpdate.as_view()),
    path('api/typedetail/<int:pk>/', TypeAPIDetailView.as_view()),
    path('api/animalslist/', AnimalsAPIList.as_view()),
    path('api/animals/<int:pk>/', AnimalsAPIUpdate.as_view()),
    path('api/animalsdetail/<int:pk>/', AnimalsAPIDetailView.as_view())
]