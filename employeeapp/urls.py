from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addem", views.addem, name="addem"),
    path("empf/<id>", views.empf, name="empf"),
    path("delete/<id>",views.delete, name= "delete"),
]
