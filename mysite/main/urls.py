from django.conf.urls import url

from . import views

urlpatterns = [
    url("<int:id>", views.index, name="index"),
    url("home/", views.home, name="home"),
    url("create/", views.create, name="create"),
    url("view/", views.view, name="view"),
]
