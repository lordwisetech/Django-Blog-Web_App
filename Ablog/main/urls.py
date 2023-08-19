
from .views import Homepage,Blogpage,updatepost_view1
from django.urls import path
from .import views

urlpatterns = [
    path('',Homepage.as_view(), name="home"),

    path('blogpost/<int:pk>',Blogpage.as_view(), name="blogg"),

    path('hello',views.show),

    path('administ/',views.admindashboard, name="adminurl"),

    path('choose blog post/',updatepost_view1.as_view(),name="choose"),

    path('edit/<int:pk>', views.edit_blog, name="edit"),

    path('delete/<int:pk>', views.delete, name="delete")

]
