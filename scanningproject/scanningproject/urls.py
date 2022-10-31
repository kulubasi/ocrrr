"""scanningproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from scannerapp import views
# from members import urls as members_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('process_image/', views.process_image, name='process_image'),
    #path('upload/',views.upload, name="upload_image"),
    path('books/',views.book_list, name="book_list"),
    # path('books/upload/',views.upload_book, name="upload_book"),
    path('h',views.upload, name="imgupload"),
    path('uploadpdf/',views.uploadpdf, name="pdfupload"),
    path('uploadpdfimage/',views.pdf2img2txt, name="pdf2img2txt"),
    # path('scan/',views.scan, name="scan"),
    # path('', include('scannerapp.urls')),
    path('download/',views.download,name="downloader"),
    path('pdfdownload/',views.pdfdownload,name="pdfdownloader"),
    path('ready/',views.ready,name="ready"),
    path('pdfready/',views.pdfready,name="pdfready"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name = "home"),
    path('home/login/',views.login_user,name="login"),
    path('home/signup/',views.signup,name="signup"),
    path('home/profile/',views.profile,name="profile"),
    path('home/logout/',views.logout_user,name="logout"),
    # path('members/', include('members.urls')),   #adding the members's app URLs to the project’s URLs
]

if settings.DEBUG:#This is just for development purposes, dont use it in production
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
