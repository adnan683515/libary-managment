
from django.urls import path
from account_app import views


urlpatterns = [
    path("register/",views.register_view.as_view(),name='register'),
    path("login/",views.log_in_view.as_view(),name='log_in'),
    
    path("deposit/",views.Deposit_view.as_view(),name='deposit'),
    
    path("logout/",views.log_OUt,name='log_out')
]
