from django.urls import path  
from .views import home, activate ,signup
urlpatterns = [  
    path('', home, name = 'home'),
    path('form/', signup,name='signup'),    
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate'),  
] 