from django.contrib import admin
from django.urls import path
from ProfileApp import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.home, name='home'),
    path('home',view.home, name='home'),
    path('personalRecord',view.personalRecord,name='personalRecord'),
    path('educationalRecord',view.educationalRecord,name='educationalRecord'),
    path('interests',view.interests,name='interests'),
    path('dreamJob',view.dreamJob,name='dreamJob'),
    path('roleModel',view.roleModel,name='roleModel'),
    path('showMydata',view.showMydata,name='showMydata'),
    path('lisProduct',view.lisProduct,name='lisProduct'),
    path('inputproduct',view.inputproduct,name='inputproduct')
]