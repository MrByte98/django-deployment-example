from django.urls import path
from . import views

#templates tagging
app_name = 'basic_app'


urlpatterns = [
    ##path('',views.index,name='index'),
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
    path('help/',views.relative,name='help'),
]
