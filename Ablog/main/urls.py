from django.conf import settings
from django.conf.urls.static import static
from .views import Homepage,Blogpage,updatepost_view1,images
from django.urls import path
from .import views

urlpatterns = [
    path('',Homepage.as_view(), name="home"),
    path('images/',views.images, name="images"),

    path('blogpost/<int:pk>',Blogpage.as_view(), name="blogg"),

    path('hello',views.show),

    path('administ/',views.admindashboard, name="adminurl"),

    path('choose blog post/',updatepost_view1.as_view(),name="choose"),

    path('edit/<int:pk>', views.edit_blog, name="edit"),

    path('delete/<int:pk>', views.delete, name="delete")

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
