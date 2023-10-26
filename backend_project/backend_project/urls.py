"""
URL configuration for backend_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from backend_app import views as backend_app_views
# from accounts import views as accounts_views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'urls', backend_app_views.URLViewSet, basename='urls')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('url/', include('backend_app.urls')),
    # path('login/', accounts_views.LoginView.as_view(), name='login'),
    path('logout/', backend_app_views.LogoutView.as_view(), name ='logout'),
    path('token/', 
        backend_app_views.CustomTokenObtainPairView.as_view(), 
        name ='token_obtain_pair'),
    path('token/refresh/', 
        jwt_views.TokenRefreshView.as_view(), 
        name ='token_refresh')
]