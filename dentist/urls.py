
from django.contrib import admin
from django.urls import path,include
admin.site.site_header = " Dento admin"
admin.site.site_title = " Admin Portal"
admin.site.index_title = "Welcome to  Dento Researcher Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
]
