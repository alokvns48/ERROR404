from django.contrib import admin
from django.urls import path, include, re_path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('api/places/', views.PlaceList.as_view()),
    path('api/places/<pk>', views.PlaceDetail.as_view()),


    path('api/categories/', views.CategoryList.as_view()),
    path('api/categories/<pk>', views.CategoryDetail.as_view()),


]
