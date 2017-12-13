"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from .routers import router
from online_test import views
from django.contrib import admin
from django.urls import reverse_lazy
from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView

admin.site.site_title = 'Candidate Evaluation System'
admin.site.site_header = 'Candidate Evaluation System'
admin.site.index_title = 'Test Administration'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^$', views.home_page, name='home_page'),
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    url(r'^', include('online_test.urls')),
]
