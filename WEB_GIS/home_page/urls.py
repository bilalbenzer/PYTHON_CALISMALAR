from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name = "index"),
    path("simdi/",views.simdikizaman, name ="simdikizaman"), 
]