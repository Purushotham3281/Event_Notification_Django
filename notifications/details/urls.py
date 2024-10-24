from django.urls import path
from details import views

urlpatterns=[
    path("insert",views.fun1),
    path("search",views.fun2),
    path("delete",views.fun3)
]