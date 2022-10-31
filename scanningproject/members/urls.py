# from django.urls import path, include
# from members import views
# urlpatterns = [path('', views.home, name = "home"),
#     ]


from django.urls import path
from members import views
urlpatterns = [

 path('h', views.home, name = "home"),
]


# from django.contrib import admin
# from django.urls import path,include
# urlpatterns = [
# path('admin/', admin.site.urls),
# path('accounts/', include('django.contrib.auth.urls')),
# ]