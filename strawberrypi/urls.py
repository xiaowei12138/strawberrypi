"""strawberrypi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from TI_gui import views as gui_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',gui_view.main_index,name = 'main_index'),
    path('xiala1/',gui_view.xiala1,name = 'xiala1'),
    path('xiala2/',gui_view.xiala2,name= 'xiala2'),
    path('other1/',gui_view.other,name = 'other1'),
    path('otherselect/',gui_view.otherselect,name = 'otherselect'),
    path('tuxiangjiexi/',gui_view.tuxiangjiexi,name = 'tuxiangjiexi'),
    path('shishishuju/',gui_view.shishishuju,name = 'shishishuju'),
    path('shujufenxi/',gui_view.shujufenxi,name = 'shujufenxi'),
    path('shujudaoru/',gui_view.shujudaoru,name = 'shujudaoru'),
    path('main_index/',gui_view.main_index,name = 'main_index'),
    path('abnormal/',gui_view.abnormal,name = 'abnormal'),
    #path('data/',gui_view.data,name = 'data'),
    path('real-time/',gui_view.real_time,name = 'real_time'),
    path('video/',gui_view.video,name = 'video'),
    path('etiological_analysis/',gui_view.etiological_analysis,name = 'etiological_analysis'),
    path('data_anomaly_analysis/',gui_view.data_anomaly_analysis,name = 'data_anomaly_analysis')
]
urlpatterns   += staticfiles_urlpatterns()
