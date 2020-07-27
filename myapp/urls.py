from django.urls import path
from . import views
app_name="myapp" #is used to create a namespace #this line is not mandatory if u wan you can add it
#i added the app name line just for understanding.

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='Home'),
    path('fact/<n>',views.fact,name='factorial'),
    path('child/',views.child,name="Child"), #path("secondarysuffix",address of function,name of mapping)
    
]
