from django.urls import  path
from  . import  views

urlpatterns = [
    path("",views.home,name = "home"),
    path("employees/",views.employees,name = "employees"),
    path("analytics/",views.analytics,name ="analytics"),
    path("search/",views.search, name = "search"),
    path("about/",views.about , name = "about"),
]