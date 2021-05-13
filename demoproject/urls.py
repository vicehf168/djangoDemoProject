"""demoproject URL Configuration

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
from django.contrib import admin
from django.urls import path,include
#函数在demoapp模块下，与当前文件不在同一个路径，因此先引入views所在模块的包，才能使用views中的方法
from demoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage),
    path('demoapp/', include('demoapp.urls')),  #表示路径以demoapp的去demoapp.urls里找对应的views
    # path('home/(\d{4})', views.home),  #(\d{4})是一个正则表达式，()表示分组，\d{4}表示4位数字，整体表示路径home/后面跟上4位数字，才能匹配上
]
