"""django_example_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from catalog import views
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

# Add homework 8. Triangle view.
urlpatterns += [
    path('triangle/', include('triangle.urls')),
]


# Homework 9. Add URLConf to create, view Persons
urlpatterns += [
    path('person/', views.person_view, name='person-create'),
    path('person/<int:pk>/', views.person_detail, name='person-detail'),
]

# Homework 12.
if settings.DEBUG:
    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls)),  # Add Debug Tollbar's URLconf
        path('silk/', include('silk.urls', namespace='silk')),  # Add Silk's URLconf
    ]
