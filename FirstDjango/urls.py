"""FirstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin

# from django.urls import path
#
# from MainApp import views
#
# urlpatterns = [
#     path('', views.main),
#     path('/about', views.about),
# ]
# from django.contrib import admin

# from django.urls import path
# from MainApp import views
#
# urlpatterns = [
#     path('', views.main),
#     path('items/', views.items_list),
#     path('item/<int:id>/', views.item),
#     # path('/about', views.about),
# ]
# from django.conf import settings
# from django.conf.urls.static import static
#
#
# urlpatterns = [
#    path('admin/', admin.site.urls),
# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.main, name="home-page"),
    path('items/', views.items_list, name="items-list"),
    path('item/<int:id>/', views.item, name="item-page"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



