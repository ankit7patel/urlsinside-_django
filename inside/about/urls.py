from django.urls import path
# from .views import home     #1
from about import views




urlpatterns = [
    # path('home/',home)    #1
    path('',views.about)
    

]