from django.contrib import admin
# Add the include function to the import
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
  path('', include('main_app.urls')),
  # include the built-in auth urls for the built-in views
  path('accounts/', include('django.contrib.auth.urls')),

]