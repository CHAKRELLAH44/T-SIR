from django.urls import path,include
from . import views

urlpatterns = [
    path('tableaux/',views.tableaux_C,name='tableaux_C'),
    path("addrid/",views.addrid,name="addrid"),
    path("ridestatus/<int:pk>",views.ridestatus,name="ridestatus"),
    path('acceptride/<int:pk>',views.accept_ride,name='accept_ride'),
    path('declineride/<int:pk>',views.decline_ride,name='decline_ride'),
    
    
]
