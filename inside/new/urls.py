from django.urls import path
# from .views import home     #1
from new import views




urlpatterns = [
    # path('home/',home)    #1
    path('',views.home)
    

]