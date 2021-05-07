import debug_toolbar
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
