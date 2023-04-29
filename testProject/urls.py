"""
URL configuration for testProject project.

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
from django.conf.urls.static import static
from testProject import settings
from tree_menu.views import HomeView, BlogView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', BlogView.as_view(), name='blog'),
    path('', HomeView.as_view(), name='home'),
    path('main_menu/', HomeView.as_view(), name='main_menu'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
